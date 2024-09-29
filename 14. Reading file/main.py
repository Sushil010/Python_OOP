import json
import csv

# file_path="C:/Users/DELL/Desktop/hello.txt"
# file_path="C:/Users/DELL/Desktop/hello.json"
file_path="C:/Users/DELL/Desktop/hello.csv"

try:
    with open(file_path,"r") as file:
        readerer=csv.reader(file)
        
        for woo in readerer:
            # for printing a specific column of data
            print(woo[0])
            # print(woo)
        # provides a memory address instead
        # print(readerer)

        # loader=json.load(file)
        # print(loader["name"],loader["age"])
        # print(loader)

        # for txt file
        # content=file.read()
        # print(content)

except FileNotFoundError:
    print("Unable to access file link")