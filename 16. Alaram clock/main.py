import datetime
import time
import pygame

class Alarm:
    def __init__(self,hour,min,sec):
        self.hour=hour
        self.min=min
        self.sec=sec

    def start_timer(self):
        alarm=f"{self.hour:02}:{self.min:02}:{self.sec:02}"
        run=True
        while run:
            current_time=datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time)
            if(current_time==alarm):
                print("Wake UP🚘🚘🚘🚔🚑")            
                run=False
            time.sleep(1)

        # current=datetime.datetime.now()
        # if current.hour==self.hour and current.minute == self.min:
        #     print("it's time")
        # else:
        #     print(current)
        #     print("no time")

alarm=input("Enter the time to wake up (HH:MM:SS): ")
houred,minut,sec=map(int,alarm.split(":"))
alarmed=Alarm(houred,minut,sec)
alarmed.start_timer()
