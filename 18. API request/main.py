import requests



class get_info:
    baseUrl="https://pokeapi.co/api/v2/" 

    def __init__(self,name):
        self.name=name

    def get_status(self):
        fullUrl= f"{get_info.baseUrl}/pokemon/{self.name}"  
        response=requests.get(fullUrl)
        result=response.json()
        
        if response.status_code==200:
            print("Data retreived!")
        else:
            print(f"Unable to load data error {response.status_code}")
        
        return(result)
        

        


pok_name=input("Enter name of pokemon: ")
name=get_info(pok_name)
value=name.get_status()



print(f"Name: {value['name'].capitalize()}")
print(f"Height: {value['height']}")
print(f"weight: {value['weight']}")
print(f"ID: {value['id']}")