import requests
from bs4 import BeautifulSoup

first_URL = "https://vm009.rz.uos.de/crawl/index.html"
stack_crawler = [first_URL]

indexing_dic = {}

# GET request 
#response = requests.get(stack_crawler.pop())
#print(response.text)  # prints the request body (here: HTML content)
#print(response.headers)
#print(response.content)


#soup = BeautifulSoup(response.content, 'html.parser') # defualt parser html parser
#print(soup.title)
#print(soup.title.text)
#print(soup.prettify())

"""# to find all links (always start with <a ...)
for l in soup.find_all("a"):
    #print(l)
    #print(l.text)
    print(l['href']) # extract URLs from link
"""

# while stack not empty
while len(stack_crawler) != 0:
    URL = stack_crawler.pop()
    # If not visited frequently -> IMPLEMENTATION NEEDED ("update visited list")
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    for l in soup.find_all("a"):
        stack_crawler.append(l['href']) # Invalid URL 'page3.html': No schema supplied.
        print(l['href'])



