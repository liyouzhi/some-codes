import datetime

dates = {}

def init_dates(dates):
    start_date = datetime.date(2017,1,1)
    for i in range(365):
        deltadays = datetime.timedelta(days=i+1)
        date = start_date + deltadays
        dates[date]=0


init_dates(dates)
print(dates)
