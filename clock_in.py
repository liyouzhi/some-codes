# -*- coding:utf-8 -*-
import logging
import sys
import calendar

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

# :TODO def init_dates(dates):

# :TODO def clock_in():

# :TODO set_dates(dates):
    
setup_logging()
app = Bottle()

if __name__ == '__main__':
    app.run(host='localhost', port=8000, reloader=True)
