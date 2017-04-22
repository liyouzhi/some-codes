# -*- coding:utf-8 -*-
import logging
import sys
import datetime

from bottle import run, route, Bottle


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
    for i in range(365):
        deltadays = datetime.timedelta(days=i+1)
        date = start_date + deltadays
        dates[date]=0

def clock_in():
    # get check_box
    if check_box == 1:
        today = datetime.date.today()
        dates[today] = 1

# :TODO set_dates(dates):
    
setup_logging()
app = Bottle()

if __name__ == '__main__':
    app.run(host='localhost', port=8000, reloader=True)
