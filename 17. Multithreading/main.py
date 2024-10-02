import threading
import time

class tasks:

    def __init__(self,name):
        self.name=name

    def walk_dog(self):
        time.sleep(1)
        print(f"Dog walk has completed of {self.name}")

    def trash_takeout(self):
        time.sleep(3)
        print("Trash has been taken out")

    def get_mail(self):
        time.sleep(4)
        print("Mail accessed")



Task=tasks("MYDOG")
# Task.walk_dog()
# Task.trash_takeout()
# Task.get_mail()



first=threading.Thread(target=Task.walk_dog)
first.start()


second=threading.Thread(target=Task.trash_takeout)
second.start()


third=threading.Thread(target=Task.get_mail)
third.start()




# a join fucntion is needed before completing other program as other will execute first
first.join()
second.join()
third.join()

print("All completed!")