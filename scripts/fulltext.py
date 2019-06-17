import json
import urllib

fulltext = []

with open("fulltext_links.txt") as file:
    content = file.readlines()

content = [x.strip() for x in content] 
content = filter(None, content)

for link in content:
    response = urllib.urlopen(link)
    data = json.load(response)
    fulltext.append(data['value'])

fulltext = [x.encode('utf-8') for x in fulltext]


with open('fulltext.txt', 'w') as outfile:  
    for item in fulltext:
        outfile.write("%s\n" % item) 
