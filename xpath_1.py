from lxml import etree
file = etree.parse("movies.xml")
root = file.getroot()
entries=file.xpath("//Title")
mp = {}
i=0
for child in entries:
    try:
        a=entries[i].values()[0]
    except IndexError:
        a="None"
    mp[child.text] = a
    i+=1
for i in mp:
    print(i + " runtime = " + mp[i])