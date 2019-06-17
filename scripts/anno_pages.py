import json
import urllib

anno_links = []

with open("manifest_links.txt") as file:
    content = file.readlines()

content = [x.strip() for x in content] 

for link in content:
    response = urllib.urlopen(link)
    data = json.load(response)  
    try:
        num_entries = len(data['sequences'])
    except Exception as e:
        print repr(e)
    
    try:
        for x in range(num_entries):
            for i in data['sequences'][x]['canvases'][x]['otherContent']:
                anno_links.append(i['@id'])
    except Exception as e:
        print repr(e)
        
    try:
        for x in range(num_entries):
             for i in data['sequences'][x]['canvases'][x]['images']:
                anno_links.append(i['@id'])
    except Exception as e:
        print repr(e)

print anno_links

with open('anno_links.txt', 'w') as outfile:  
    for item in anno_links:
        outfile.write("%s\n" % item) 
