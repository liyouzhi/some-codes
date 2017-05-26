# -*- coding:utf-8 -*-

import json
from datetime import datetime

data = {
        datetime(2017,1,2).timestamp() : 1,
        datetime(2017,2,3).timestamp() : 1,
        datetime(2017,3,3).timestamp() : 1,
        datetime(2017,4,3).timestamp() : 1,
        datetime(2017,5,3).timestamp() : 1,
        datetime(2017,6,3).timestamp() : 1,
        datetime(2017,7,3).timestamp() : 1,
        datetime(2017,8,3).timestamp() : 1,
        datetime(2017,9,3).timestamp() : 1,
        datetime(2017,10,3).timestamp() : 1,
        datetime(2017,11,3).timestamp() : 1,
        datetime(2017,12,3).timestamp() : 1,
        datetime(2017,11,9).timestamp() : 1,
        datetime(2017,4,1).timestamp() : 1,
        datetime(2017,4,30).timestamp() : 1,
        datetime(2017,2,28).timestamp() : 1,
        datetime(2017,4,26).timestamp() : 1,
        datetime(2017,8,8).timestamp() : 1,
        datetime(2017,10,24).timestamp() : 1,
        datetime(2017,9,1).timestamp() : 1,
        datetime(2017,11,18).timestamp() : 1,
        datetime(2017,11,11).timestamp() : 1,
        datetime(2017,11,12).timestamp() : 1,
        datetime(2017,4,20).timestamp() : 1,
        datetime(2017,11,28).timestamp() : 1,
        datetime(2017,2,6).timestamp() : 1,
        datetime(2017,5,23).timestamp() : 1,
        datetime(2017,5,1).timestamp() : 1
        }

json_data = json.dumps(data)
with open('/Users/liyouzhi/dev/python/some-codes/clock_in/data/cal_data.json', 'w') as f:
    f.write(json_data)



