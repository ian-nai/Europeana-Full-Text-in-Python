import urllib
import json

class Search(object):
    
    @staticmethod
    def search(*args):
       
        anno_links = []
        full_links = []
       
        for arg in args:
            search_string = ('+'.join('' + item + '' for item in args))
   
        API_key = "your_key"
        base_url = "https://newspapers.eanadev.org/api/v2/search.json?query="
        url = "".join(base_url + '' + search_string + '' + "&profile=hits&wskey=" + API_key)

        print url
        response = urllib.urlopen(url)
        data = json.load(response) 
        try:
            num_entries = len(data['items'])
        except Exception as e:
            print repr(e)
   
        try:
            for i in data['items']:
                anno_links.append(i['id'])
        except Exception as e:
            print repr(e)
            

        for base in anno_links:
           base_url2 = "https://iiif.europeana.eu/presentation"
           new_url = "".join(base_url2 + '' + base_thing + '' + "/annopage/1")
           full_links.append(new_url)
      
        text_links = []
        print full_links
        for link in full_links:
           response2 = urllib.urlopen(link)
           data2 = json.load(response2) 
           try:
               num_entries2 = len(data2['resources'])
           except Exception as e:
               print repr(e)
        
           try:
               for i in data2['resources']:
                    text_links.append(i['resource']['@id'])
           except Exception as e:
               print repr(e)
        
        fulltext = []
        print text_links
        
        for txt in text_links:
            response3 = urllib.urlopen(txt)
            data3 = json.load(response3)
            fulltext.append(data3['value'])
      
      
        fulltext = [x.encode('utf-8') for x in fulltext]


        with open('fulltext.txt', 'w') as outfile: 
           for item in fulltext:
               outfile.write("%s\n" % item)
