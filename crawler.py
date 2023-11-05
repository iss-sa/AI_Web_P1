import requests
from bs4 import BeautifulSoup

first_URL = "https://vm009.rz.uos.de/crawl/index.html"
stack_crawler = [first_URL]

dickk = {"ilva": ["no dic"]}
dickk['ilva'].append("nio")
lst = dickk.get("ilva")
print(lst)

indexing_dic = {}

# while stack not empty
while len(stack_crawler) != 0:
    URL = stack_crawler.pop()
    # If not visited frequently -> IMPLEMENTATION NEEDED ("update visited list")
    res = requests.get(URL)
    soup = BeautifulSoup(res.content, "html.parser")
    text = soup.find_all(text = True)
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

    print(keys)

    for key in keys:
        if key not in indexing_dic.keys():
            indexing_dic[key] = [URL]
        else:
            indexing_dic[key].append(URL)
    
    for l in soup.find_all("a"):
        stack_crawler.append(l['href']) # Invalid URL 'page3.html': No schema supplied.

        print(l['href'])