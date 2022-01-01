import requests 
url="http://www.google.com"
r=requests.get(url)
print(r.content)