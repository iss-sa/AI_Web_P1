import requests
from bs4 import BeautifulSoup

first_URL = "https://vm009.rz.uos.de/crawl/index.html"
stack_crawler = [first_URL]
visited_lst = []

indexing_dic = {}


# while stack not empty
while len(stack_crawler) != 0:
    URL = stack_crawler.pop()
    # If not visited yet, visit website
    if (URL not in visited_lst):

        visited_lst.append(URL)

        res = requests.get(URL, allow_redirects=False)
        soup = BeautifulSoup(res.content, "html.parser")
        text = soup.find_all(string = True)
        output = ''
        blacklist = [
            '[document]',
            'noscript',
            'header',
            'html',
            'meta',
            'head', 
            'input',
            'script',
        # name more elements if not required
        ]
        for t in text:
            if t.parent.name not in blacklist:
                output += '{} '.format(t)

        output_lst = output.split()

        keys = []
        for word in output_lst:
            if word not in keys:
                keys.append(word)
            else:
                continue

        #print(keys)

        for key in keys:
            if key not in indexing_dic.keys():
                indexing_dic[key] = [URL]
            else:
                indexing_dic[key].append(URL)
        
        #print(indexing_dic)
        
        for l in soup.find_all("a"):
            stack_crawler.append(requests.compat.urljoin('https://vm009.rz.uos.de/crawl/index.html', l['href'])) 

query = input("What is your query?")

query_lst = query.split()
print(query_lst)

query_app_lst = []
for word in query_lst:
    query_app_lst += indexing_dic[word]
print(query_app_lst)

answer = [w for w in query_app_lst if query_app_lst.count(w)>(len(query_lst) -1)]
answer_unique = set(answer)
print(answer_unique)

