# txt_data="Hello there !!!"

import json
import csv

# data={
#     "name":"void",
#     "age":90,
#     "type":"galaxy"
# }

# txt_data=["this","is","just","a","collection"]

csv_data=[
    ["Name","Age","Job"],
    ["Void",200,"NOthing"],
    ["Null",300,"Anything"],
    ["Exit",100,"Here"]
]


file_path="C:/Users/DELL/Desktop/hello.csv"

try:
    with open(file_path,"w",newline="")as file:
        writer=csv.writer(file)
        for row in csv_data:
            writer.writerow(row)
        # json.dump(data,file,indent=4)
        # for name in txt_data:
        #     file.write(name+"\n")
        print(f"CSV file at {file_path} was created")

except FileExistsError:
    print("File already exists")
