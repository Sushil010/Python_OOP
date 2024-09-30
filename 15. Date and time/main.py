import datetime


# anydate=datetime.date(2024,12,10)
# date=datetime.date.today()
# print(date)
# print(anydate)


# nowtime=datetime.datetime.now()
# nowtime=nowtime.strftime("%H:%M:%S  %m-%d-%Y")


# print(nowtime)


target_datetime=datetime.datetime(2020,10,12, 9,12,1)
current_datetime=datetime.datetime.now()

if target_datetime<current_datetime:
    print(f" Provided {target_datetime} Time and date passed")
else:
    print(f"Provided {target_datetime} Yet to come")