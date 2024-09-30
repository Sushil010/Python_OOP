import datetime

class Alarm:
    def __init__(self,hour,min):
        self.hour=hour
        self.min=min

    def start_timer(self):
        current=datetime.datetime.now()
        if current.hour==self.hour and current.minute == self.min:
            print("it's time")
        else:
            print(current)
            print("no time")

alarm=Alarm(13,45)
alarm.start_timer()
