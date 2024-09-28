
def additional_element(func):
    def wrapper(*args, **kwargs):
        print("Returning first element 👀")
        func(*args, **kwargs)
    return wrapper

def remaining_element(func):
    def wrap(*args, **kwargs):
        print("Returning second element 🐱‍👤")
        func(*args, **kwargs)
    return(wrap)



@additional_element
@remaining_element
def get_element(ran):
    print(f"Here is your requested {ran} element ❄")


get_element("random")