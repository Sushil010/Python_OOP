
# include a wrapper function, else without calling function statement will get printed
# even while only including decorators(used to increase functionality of base function)



# def before_play(func):
#     def wrap():
#         print("wear shoes")
#         func()
#     return wrap


# @before_play
# def play():
#     print("Playing done")

# play()



def before_play(func):
    def wrap(*args,**kwargs):
        print("wear shoes")
        func(*args,**kwargs)
    return wrap


@before_play
def play(param):
    print(f"Played {param}")



play("Football")