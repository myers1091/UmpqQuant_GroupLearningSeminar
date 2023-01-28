import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.allrecipes.com/recipe/9889/seven-layer-bars/'
page = requests.get(url)
html_test = page.text
soup = BeautifulSoup(html_test,'html.parser')
#  for link in soup.find_all('script'):
#      print(link.get('recipeIngredient'))
ing=''
texts = soup.find_all('script')
for text in texts:
    # print("XXXXXXXXXXXXXXXXXXX ",len(text.get_text()))
    # print(text.get_text())
    # # if len(text.get_text())>5000:
    try:
        ing = re.search('(?<=\"recipeIngredient\":) (.+\n.)+(?=\"recipeInstructions\")',text.get_text()).group(0)[2:-3]
        ing_list  = ing.split(sep=",")
        print(ing_list[0])
    except AttributeError:
        pass
    
