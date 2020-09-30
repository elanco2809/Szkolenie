import datetime
import time

today = datetime.datetime.today()
print(today)

curr_time = datetime.datetime.now().time()
print(curr_time)

day_of_week = datetime.date.weekday(today)
print(day_of_week)

birth_day = datetime.datetime(1976, 8 ,15, 6, 0, 0)
print(birth_day.strftime("%m/%d/%Y"))

curr_time = datetime.datetime.now().time()
print(curr_time.strftime("%H:%M:%S"))

diff = today - birth_day
print(f"Przeżyłeś {diff.days} dni")

print(time.time())
print(time.time_ns())