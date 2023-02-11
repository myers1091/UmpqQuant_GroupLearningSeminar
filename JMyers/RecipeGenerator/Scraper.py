#!/usr/bin/env python3
import requests
import re
from bs4 import BeautifulSoup

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
            ing = ing.replace("\n","").replace("\"","")
            ing_list  = ing.split(sep=",")
        
        except AttributeError:
            pass
    #print(len(ing_list))
    entry = [title.string,ing_list]      
    return(entry)
    
dataset  = []
#urllist = ['https://www.allrecipes.com/food-news-trends/trends/']

urllist = ['https://www.allrecipes.com/recipe/9889/seven-layer-bars/'\
    ,'https://www.allrecipes.com/food-news-trends/trends/']
for website in urllist:
    xy_pair = grab_entry(website)
    if len(xy_pair[1]):
        dataset.append(xy_pair)




print(dataset)


