# 3.	Write a program to find difference between two given dates 
# and time (format of the input will be like time 1 : dd/mm/yyyy hh:mm:ss. Time 2 : dd/mm/yyyy hh:mm:ss)

import datetime
from datetime import timedelta

datetimeFormat = '%d/%m/%Y %H:%M:%S'
date1 = input('time 1:')
date2 = input('time 2:')
# date1 = '10/03/2016 09:56:28'
# date2 = '16/04/2016 10:01:28'

diff = abs(datetime.datetime.strptime(date1, datetimeFormat) - datetime.datetime.strptime(date2, datetimeFormat))
 
print("Difference:", diff)
