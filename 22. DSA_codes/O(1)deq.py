from collections import deque
class stacks:

    
    def __init__(self):
        self.queue=deque()

    # def push(self):
    #     stacks.lists.append(self.num)
    #     print(f"Number {self.num} has been pushed into stack")

    # def poper(self):
    #     popped_no=stacks.lists.pop()
    #     print(f"Number {popped_no} has been popped out")

    # def __init__(self):
    #     pass

    def push(self,num):
        for nums in num:
            self.queue.append(nums)
            print(f"Number {nums} has been appended")

    def poper(self,iter):
        for _ in range(iter):
            popped_no =self.queue.pop()
            print(f"Number {popped_no} has been popped out")


   


Stacks=stacks()
Stacks.push([1,2,4,3,5])
Stacks.poper(3)
# Stacks.poper()
# Stacks.poper()
# Stacks.poper()
print(list(Stacks.queue))


