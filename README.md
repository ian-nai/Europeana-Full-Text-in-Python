# Europeana Full Text in Python
Various Python scripts to assist with searching and downloading full text records via the [Europeana](https://www.europeana.eu/portal/en) APIs.
These scripts allow you to search records in Europeana, parse the JSON returned to obtain various metadata, and download full text if it's available.

### Getting Started

Sign up for a Europeana API key [here.](https://pro.europeana.eu/get-api)

Then launch Python to start searching.

### Searching

The ["search.py"](https://github.com/ian-nai/Europeana-Full-Text-in-Python/blob/master/scripts/search.py) script allows you to search in Europeana and return the results in JSON.

Example usage:
```
>>> from search import Search
>>> Search.search('your', 'keywords')
````
This will return the JSON of your search's results. The JSON file will be saved locally for easy parsing. By default, this script returns 100 results.

### Other Scripts

The other scripts work together to retrieve the full text (when available) and additional metadata of items returned by a search query.

You can also feed specific items to the scripts to retrieve their full text.

Starting with ["manifest.py"](https://github.com/ian-nai/Europeana-Full-Text-in-Python/blob/master/scripts/manifest.py), input your search terms like so:

```
>>> from manifest import Search
>>> Search.search('your', 'keywords')
```

This will save a list of manifest links for use in other scripts, or for your own reference. To continue, run the [anno_pages.py](https://github.com/ian-nai/Europeana-Full-Text-in-Python/blob/master/scripts/anno_pages.py), [annotations.py](https://github.com/ian-nai/Europeana-Full-Text-in-Python/blob/master/scripts/annotations.py), [text_links.py](https://github.com/ian-nai/Europeana-Full-Text-in-Python/blob/master/scripts/text_links.py), and [fulltext.py](https://github.com/ian-nai/Europeana-Full-Text-in-Python/blob/master/scripts/fulltext.py) scripts from your console:

```
>>> python anno_pages.py
>>> python annotations.py
>>> python text_links.py
>>> python fulltext.py
```
Once the final script has run, you should have the full text of the items you've requested.

### All-in-one

The ["all_in_one.py"](https://github.com/ian-nai/Europeana-Full-Text-in-Python/blob/master/scripts/all_in_one.py) script allows you to search in Europeana and return any available full text from the results, with all of the scripts combined into one file.

Example usage:
```
>>> from all_in_one import Search
>>> Search.search('your', 'keywords')
````

### Newspapers

The ["newspaper_search.py"](https://github.com/ian-nai/Europeana-Full-Text-in-Python/blob/master/newspapers/newspaper_search.py) script allows you to search newspapers in Europeana and return any available full text from the results, with all of the text combined into one .txt file.

Example usage:
```
>>> from newspaper_search import Search
>>> Search.search('your', 'keywords')
````
