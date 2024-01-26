import requests
url="https://www.geeksforgeeks.org/data-structures/"
respons=requests.get(url)
data=respons.text.split()
for i in data:
    print(i)