class queue:
    lists=[]
    # def __init__(self,num):
    #     self.num=num

    # def push(self):
    #     stacks.lists.append(self.num)
    #     print(f"Number {self.num} has been pushed into stack")

    # def poper(self):
    #     popped_no=stacks.lists.pop()
    #     print(f"Number {popped_no} has been popped out")

    def __init__(self):
        pass

    def push(self,num):
        for nums in num:
            queue.lists.append(nums)
            print(f"Number {nums} has been appended")

    def poper(self,iter):
        for _ in range(iter):
            popped_no =queue.lists.pop(0)
            print(f"Number {popped_no} has been popped out")


   


Queue=queue()
Queue.push([1,2,4,3,5])
Queue.poper(1)
# Queue.poper()
# Queue.poper()
# Queue.poper()
print(Queue.lists)


