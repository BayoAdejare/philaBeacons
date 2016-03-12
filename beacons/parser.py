from lxml import html
import requests

page = requests.get('http://www.philamuseum.org/collections/socialTagging.html')
tree = html.fromstring(page.content)

print (page)
print (tree)

