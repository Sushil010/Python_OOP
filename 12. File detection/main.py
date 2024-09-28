import os


file_path="12. File detection/test.txt"
# print(os.getcwd())

if os.path.exists(file_path):
    print(f"The provided path '{file_path}' exists ")
else:
    print("Location can't be found")