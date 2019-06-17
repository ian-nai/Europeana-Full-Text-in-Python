import json
import urllib

annotations = []

with open("anno_pages.txt") as file:
    content = file.readlines()
    
content = [x.strip() for x in content] 
 
 
for link in content:
    response = urllib.urlopen(link)
    data = json.load(response)
    for i in data['resources']:
        annotations.append(i['@id'])
        
with open('annotations.txt', 'w') as outfile:  
    for item in annotations:
        outfile.write("%s\n" % item) 
