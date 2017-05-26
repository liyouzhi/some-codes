# -*- coding:utf-8 -*-
import logging
import sys
import datetime

from bottle import run, route, Bottle, HTTPResponse, template, static_file

from PIL import Image, ImageDraw, ImageFont

def setup_logging():
    FORMAT = "%(asctime)s %(levelname)s %(process)d %(message)s"
    formatter = logging.Formatter(FORMAT)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

dates = {}

def init_dates(dates):
    start_date = datetime.date(2017,1,1)
    for i in range(364):
        deltadays = datetime.timedelta(days=i+1)
        date = start_date + deltadays
        dates[date]=0

def get_weekday(date): #0-6
    return date.weekday()    

def get_order(date):
    yday = date.timetuple().tm_yday
    num = (yday+5) // 7
    return num

def clock_in():
    # get check_box
    if check_box == 1:
        today = datetime.date.today()
        dates[today] = 1
    # TODO return

def get_position(date):
    y = get_weekday(date) * 12 + 2
    x = get_order(date) * 12 + 2
    return (x,y,x+9,y+9)

def draw_calendar_graph(dates):
    color_default = (235,237,240,100)
    color_draw = (248,195,205,100) 
    graph_size = (53*12+2, 7*12+2)
    graph = Image.new('RGBA',graph_size,(255,255,255,100))
    draw = ImageDraw.Draw(graph)
    for date in dates:
        position = get_position(date)
        if dates.get(date) == 1:
            color = color_draw
        else: color = color_default
        draw.rectangle(position,fill=color)
        # print(position)
    graph.save('calendar_graph.jpg', 'jpeg')

setup_logging()
app = Bottle()

@app.route('/graph', method='GET')
def show_graph():
    with open('./calendar_graph.jpg', 'rb') as f:
        data = f.read()
    mtype = 'image/jpeg'
    res = HTTPResponse(body=data)
    res.set_header('Content-Type', mtype)
    return res

@app.route('/', method='GET')
def home():
    return template('home.html')

@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root = './static')

@app.route('/data/<filename>')
def server_data(filename):
    return static_file(filename, root = './data')

if __name__ == '__main__':
    app.run(host='localhost', port=8000, reloader=True)
