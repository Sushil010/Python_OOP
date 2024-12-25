class top:
    obj_count=0

    def __init__(self,name):
        self.name=name
        top.obj_count+=1

    @classmethod
    def obj_counted(param):
        print(f"total obj formed are {param.obj_count}")


first=top("one")
second=top("two")
top.obj_counted()