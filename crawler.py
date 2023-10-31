import requests
from bs4 import BeautifulSoup

# GET request 
response = requests.get("http://info.cern.ch/hypertext/WWW/TheProject.html")
#print(response.text)  # prints the request body (here: HTML content)
#print(response.headers)
#print(response.content)

soup = BeautifulSoup(response.content, 'html.parser') # defualt parser html parser
#print(soup.title)
#print(soup.title.text)
print(soup.prettify())

# to find all links (always start with <a ...)
for l in soup.find_all("a"):
    #print(l)
    #print(l.text)
    print(l['href']) # extract URLs from link
