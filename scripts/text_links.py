import json
import urllib

fulltext_links = []


with open("annotations.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content] 
content = filter(None, content)

   
for link in content:
    response = urllib.urlopen(link)
    data = json.load(response)
    num_entries = len(data['resources'])
    
    for x in range(num_entries):
        for i in data['resources'][x]['resource']:
            fulltext_links.append(data['resources'][x]['resource']['@id'])
   

print fulltext_links

with open('fulltext_links.txt', 'w') as outfile:  
    for item in fulltext_links:
        outfile.write("%s\n" % item) 
