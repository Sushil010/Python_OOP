try:
    number=int(input("Enter a number:  "))
    print(1/number)

except ZeroDivisionError:
    print("Can't divide by zero")

except ValueError:
    print("Enter a valid datatype")

# except Exception:
#     print("Some error occured")

finally:
    print("All operation completed")