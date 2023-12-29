import io
import requests
from lxml import etree
url = "https://ru.wikipedia.org/wiki/%D0%A4%D0%B8%D0%BB%D0%BE%D1%81%D0%BE%D1%84%D0%B8%D1%8F"
data = requests.get(url).text

parser = etree.HTMLParser()
tree = etree.parse(io.StringIO(data), parser)
for im in tree.xpath('//a'):
    print(im.get('href'))
    
    