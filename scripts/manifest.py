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
        
        with open('manifest_links.txt', 'w') as outfile:  
            for item in final_links:
               outfile.write("%s\n" % item) 
            
           
            
