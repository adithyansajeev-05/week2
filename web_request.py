import requests
url="https://jsonplaceholder.typicode.com/todos/"
response=requests.get(url)
print("ststus code : ",response.status_code)
