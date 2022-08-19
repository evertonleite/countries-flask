from re import I
from server import update
import requests

api_url = "http://127.0.0.1:8090/countries"

def get():
    response = requests.get(api_url)
    print(response.json())

def insert():
    insert = {"name": "jeremaya", "capital": "shuryma", "area": 4115}
    response = requests.post(api_url, json=insert)
    print(response.json())
    response = requests.get(api_url)
    print(response.json())

def get_by_id(id):
    api_url = f"http://127.0.0.1:8090/countries/{id}"
    response = requests.get(api_url)
    print(response.json())

def update(id):
    update = {"name": "jeremaya", "capital": "shuryma", "area": 4115}
    api_url = f"http://127.0.0.1:8090/countries/{id}"
    response = requests.put(api_url, json=update)
    print(response.json())

def delete(id):
    api_url = f"http://127.0.0.1:8090/countries/{id}"
    response = requests.delete(api_url)
    print(response)
    print(response.status_code)
    
get_by_id(3)
insert()
update(4)
delete(3)
get()

# update(5)
# delete(1)