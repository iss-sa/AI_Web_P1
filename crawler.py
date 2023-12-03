import requests
from bs4 import BeautifulSoup
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser


first_URL = "https://vm009.rz.uos.de/crawl/index.html"

# crawler including new index
def crawl(first_URL, search):
    # for indexing
    schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True))
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
            output = '' # all the content text of website
            # to exlude unwanted elements
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

            #add url and content to index writer
            writer.add_document(title=URL, content=output)
            
            # find all links on site and add to stack
            for l in soup.find_all("a"):
                stack_crawler.append(requests.compat.urljoin('https://vm009.rz.uos.de/crawl/index.html', l['href']))

    #close writer and commit all previous changes
    writer.commit()
    lst=[] # for urls
    # for titles and content of websites
    titles = []
    content = []

    # index search
    with ix.searcher() as searcher:
        # index as AND operator
        query = QueryParser("content", ix.schema).parse(search)
        corrected = searcher.correct_query(query, search) # always correct query just in case

        results = searcher.search(corrected.query)
        for r in results:
            lst.append(r["title"])
            content.append(r.highlights("content"))

        # to get the website name form the url
        for url in lst:
            title1 = url.replace("https://vm009.rz.uos.de/crawl/", "")
            title = title1.replace(".html", "")
            titles.append(title)

        return zip(lst, titles, content)