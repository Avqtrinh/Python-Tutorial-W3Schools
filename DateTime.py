import time
from datetime import datetime
import calendar
print("the two objects for date time are naive and aware")
print("aware holds details about time zone and dls")
print("the current ticks is")
print(time.time())
print("the current time is")
dt = datetime.now()
print(dt)
print("the date is")
print(dt.now().strftime('&Y-%m-%d'))
print("the local time is")
print(time.localtime(time.time()))
print("this is a calender for this month")
print(calendar.month(dt.now().year,dt.now().month))
