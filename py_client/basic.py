import requests

endpoint = "http://localhost:3000/api/"

get_response = requests.post(endpoint,params = {"rollNo":123}, json = {"title" : "Hello World!", "description" :"abc", "price" :30})

#print(get_response.text)
print(get_response.json())    