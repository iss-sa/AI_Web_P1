import requests
from bs4 import BeautifulSoup
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser

first_URL = "https://vm009.rz.uos.de/crawl/index.html"

def crawl(first_URL, search):
    # for indexing
    schema = Schema(title=TEXT(stored=True), content=TEXT)
    # Create an index in the directory indexdr (the directory must already exist!)
    ix = create_in("indexdir", schema)
    writer = ix.writer()

    # for crawling
    stack_crawler = [first_URL]
    visited_lst = []

    # while stack not empty
    while len(stack_crawler) != 0:
        URL = stack_crawler.pop()
        # If not visited yet, visit website
        if (URL not in visited_lst):

            visited_lst.append(URL)

            res = requests.get(URL, allow_redirects=False)
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

            writer.add_document(title=URL, content=output)
            
            for l in soup.find_all("a"):
                stack_crawler.append(requests.compat.urljoin('https://vm009.rz.uos.de/crawl/index.html', l['href']))

    writer.commit()
    lst=[]
    with ix.searcher() as searcher:
        # find entries with the words 'first' AND 'last'
        query = QueryParser("content", ix.schema).parse(search)
        results = searcher.search(query)
        for r in results:
            lst.append(r["title"])

        return lst
    


#answer = crawl(first_URL, "platypus")
#print(answer)