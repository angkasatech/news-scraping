import requests
from bs4 import BeautifulSoup

html_ = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'framebar'})

soup = BeautifulSoup(html_.text, 'html.parser')

popular_area = soup.find(attrs={'class':'grid-row list-content'})

titles = popular_area.findAll(attrs={'class' : 'media__title'})
images = popular_area.findAll(attrs={'class' : 'media__image'})

#print(titles)
"""
for title in titles:
    print(title.text)
"""
for image in images:
    print(image.find('a').find('img')['title'])

