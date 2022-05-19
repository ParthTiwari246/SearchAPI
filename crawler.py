import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://stackoverflow.com/questions/tagged/python?tab=newest&page="
urls = []
contents=[]
titles =[]
for page in range(1,11):    
    response = requests.get(url+str(page))
    content = BeautifulSoup(response.text,'lxml')
    links = content.findAll('a',{'class':"s-link"})
    for link in links:
        if '/questions' in link['href']:
            if 'https' not in link['href']:
                urls.append(link['href'])
                titles.append(link.text)
    excerpts = content.findAll('div',{"class":"s-post-summary--content-excerpt"})
    for excerpt in excerpts:
        contents.append(excerpt.text.strip())