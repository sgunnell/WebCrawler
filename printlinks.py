import requests as req
from bs4 import BeautifulSoup

while True:
    starting_url = input('Input Starting URL:')
    print(starting_url)
    try:
        r = req.get(starting_url)
        break
    except:
        print("Retrieval failed re-enter url")

print(r.status_code)
print(r.headers['content-type'])
soup = BeautifulSoup(r.content, 'html.parser')
count =10
tags = soup('a')
url_list = list()
for tag in tags:
    url_list.append(tag.get('href',None))
    print(tag.get('href',None))
