import requests

endpoint = "http://localhost:3000/api?class=suuuper"



get_response = requests.get(endpoint,params = {"rollNo":123}, json = {"what is age" : 26} )

#print(get_response.text)
print(get_response.json())    