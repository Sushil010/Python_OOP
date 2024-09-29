# txt_data="Hello there !!!"

import json
data={
    "name":"void",
    "age":90,
    "type":"galaxy"
}

# txt_data=["this","is","just","a","collection"]
file_path="C:/Users/DELL/Desktop/hello.json"

try:
    with open(file_path,"w")as file:
        json.dump(data,file,indent=4)
        # for name in txt_data:
        #     file.write(name+"\n")
        print(f"Json file at {file_path} was created")

except FileExistsError:
    print("File already exists")
