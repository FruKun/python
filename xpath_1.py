from lxml import etree
file = etree.parse("movies.xml")
root = file.getroot()
entries=file.xpath("//Title")
mp = {}
i=0
for child in entries:
    try:
        mp[child.text] = entries[i].values()[0]
    except IndexError:
        mp[child.text] = "None"
    i+=1
for i in mp:
    print(i + " runtime = " + mp[i])