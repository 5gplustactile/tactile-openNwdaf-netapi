import requests
import urllib.parse
import os
import json
import datetime

os.system("clear")

while True:
    nombre = input("\nJSON file path: ")

    if nombre.lower() == 'exit':
        break
    
    try:
        with open(nombre+".json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File not found")
        continue

    url_encoded_data = urllib.parse.urlencode(data, quote_via=urllib.parse.quote)

    url_encoded_data = url_encoded_data.replace("True", "true")
    url_encoded_data = url_encoded_data.replace("False", "false")

    url="http://localhost:8080/nnwdaf-analyticsinfo/v1/analytics?"+url_encoded_data.replace("%27", '%22')
    print("\ncurl -X GET '"+url+"'")
    print()


    r=requests.get(url)
    if r.status_code==200:
        print(r.status_code)
        print()
        print(json.loads(r.content))
        data=json.loads(r.content)
        with open("./response.json", "w") as f:
            json.dump(data, f, indent=4)
    elif r.status_code==204:
        print(r.status_code)
        print("No Content")
        


