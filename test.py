import clock_in
import datetime
dates = {}
clock_in.init_dates(dates)
print(dates)
date = datetime.date(2017,1,1)
dates[date] = 1
p = clock_in.get_position(date)
print(p)
date = datetime.date(2017,12,31)
dates[date] = 1
p = clock_in.get_position(date)
print(p)


dates[datetime.date(2017,4,2)] = 1
dates[datetime.date(2017,4,3)] = 1
dates[datetime.date(2017,4,24)] = 1
dates[datetime.date(2017,4,25)] = 1
dates[datetime.date(2017,2,9)] = 1
dates[datetime.date(2017,2,8)] = 1
dates[datetime.date(2017,2,7)] = 1
dates[datetime.date(2017,2,6)] = 1
dates[datetime.date(2017,1,10)] = 1
dates[datetime.date(2017,1,9)] = 1
dates[datetime.date(2017,1,8)] = 1
dates[datetime.date(2017,1,7)] = 1
dates[datetime.date(2017,1,6)] = 1
dates[datetime.date(2017,2,5)] = 1
dates[datetime.date(2017,2,1)] = 1
dates[datetime.date(2017,1,24)] = 1
dates[datetime.date(2017,1,23)] = 1
dates[datetime.date(2017,1,22)] = 1
dates[datetime.date(2017,1,21)] = 1
dates[datetime.date(2017,10,24)] = 1
dates[datetime.date(2017,9,1)] = 1
dates[datetime.date(2017,8,8)] = 1
dates[datetime.date(2017,4,26)] = 1
dates[datetime.date(2017,6,4)] = 1
dates[datetime.date(2017,2,22)] = 1
dates[datetime.date(2017,4,1)] = 1
clock_in.draw_calendar_graph(dates)
