#!/usr/bin/env python3
import requests
import re
from bs4 import BeautifulSoup
import Crawler

def clean_ingredients(data):
    list_of_removals = [r'(?!(([^"]*"){2})*[^"]*$),',"\n","\""]
    for item in list_of_removals:
        data = re.sub(item,"",data)
    data = re.sub(' +', ' ',data)
    return(data)
def grab_entry(website):
    #input: Website URL
    #Output: recipe title, ingredient list pair
    page = requests.get(website)
    html_test = page.text
    soup = BeautifulSoup(html_test,'html.parser')
    title = soup.find('title')
    texts = soup.find_all('script')
    ing_list=[]
    for text in texts:
        try:
            ing = re.search('(?<=\"recipeIngredient\":) (.+\n.)+(?=\"recipeInstructions\")',text.get_text()).group(0)[2:-3]
            ing_cleanup = clean_ingredients(ing)
            print(ing_cleanup)
            ing_list  = ing_cleanup.split(sep=",")
        
        except AttributeError:
            pass
    entry = [title.string,ing_list]      
    return(entry)
    
dataset  = []

urllist = Crawler.parse_sitemap("https://www.allrecipes.com/sitemap.xml", ["loc" ])['loc']

for website in urllist:
    xy_pair = grab_entry(website)
    if len(xy_pair[1]):
        dataset.append(xy_pair)
    break    
print(dataset)





