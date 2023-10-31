from bs4 import BeautifulSoup

# An example HTML document
html_content = "<html><head><title>The Title</title></head><body>Body content.</body></html>"

# Parsing HTML
# The BeautifulSoup class' constructor takes an HTML document as a string and a parser name
# We'll use the builtin 'html.parser'
soup = BeautifulSoup(html_content, 'html.parser')

# Accessing Tags
# The soup object has a lot of attributes that correspond to HTML nodes (imagine the HTML document as a tree!)
title_tag = soup.title
print(title_tag)  # <title>The Title</title>
# get the text content of a Tag (including possibly nested subtags' content)
print(title_tag.text)
# Whenever you want to have text content without any tags, use the .text attribute.

 
#Navigating the Tree Structure
print(soup.head.contents)  # [<title>The Title</title>]
#You can chain HTML nodes creating a path through the HTML tree.

 
#Finding Tags by Class and ID
# Suppose there's a tag <div class="info" id="main-info">Details here</div> in our HTML
info_div = soup.find('div', class_='info')
main_info_div = soup.find('div', id='main-info')
 

#Access attributes of a tag
# Suppose there's a tag <div class="info" id="main-info">Details here</div> in our HTML
info_div = soup.find('div', class_='info')
print(info_div['id'])
#The tags attrbitutes can be accessed like dictionary elements.

 

#Example: Find all headings

#For this, let’s assume the web content has various heading tags (h1, h2, …, h6).

headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
for heading in headings:
    print(heading.text)