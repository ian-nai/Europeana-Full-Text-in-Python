import urllib
import json

class Searching(object):

    @staticmethod
    def search(*args):
        
        
        for arg in args:
            search_string = ('+'.join('' + item + '' for item in args))
    
        
        API_key = "your_key"
        base_url = "https://www.europeana.eu/api/v2/search.json?query="
        url = "".join(base_url + '"' + search_string + '"' + "&rows=100&start=1&&text_fulltext=true&wskey=" + API_key)
        base2 = "https://iiif.europeana.eu/presentation"
        print url
        response = urllib.urlopen(url)
        data = json.load(response)  


        links = []
        for i in data['items']:
            print i['id']
            links.append(i['id'])
        
        final_links = []
        for line in links:
                url2 = "".join(base2 + line + "/manifest?wskey=" + API_key)
                print url2
                final_links.append(url2)
        
        anno_links = []
        fulltext_links = []
        for link in final_links:
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
            
            anno_links = [x.strip() for x in anno_links] 
            
        for link in anno_links:
           try:
               response = urllib.urlopen(link)
               data = json.load(response)
               num_entries = len(data['resources'])
           except Exception as e:
               print repr(e)
           
           try:    
               for x in range(num_entries):
                   for i in data['resources'][x]['resource']:
                       fulltext_links.append(data['resources'][x]['resource']['@id'])
           except Exception as e:
               print repr(e)
       
        fulltext = []
        for link in fulltext_links:
            try:    
               response = urllib.urlopen(link)
               data = json.load(response)
               fulltext.append(data['value'])
            except Exception as e:
               print repr(e)

        fulltext = [x.encode('utf-8') for x in fulltext]


        with open('fulltext.txt', 'w') as outfile:  
            for item in fulltext:
                outfile.write("%s\n" % item)
