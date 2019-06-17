import urllib
import json

class Search(object):
     
    @staticmethod
    def search(*args):
        
        
        for arg in args:
            search_string = ('+'.join('' + item + '' for item in args))
    
        API_key = "your_key"
        base_url = "https://www.europeana.eu/api/v2/search.json?query="
        url = "".join(base_url + '"' + search_string + '"' + "&rows=100&start=1&text_fulltext=true&wskey=" + API_key)

        print url
        response = urllib.urlopen(url)
        data = json.load(response)  
        print data
        with open('search.json', 'w') as outfile:  
           json.dump(data, outfile)
     
           
