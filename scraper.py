import requests
from bs4 import BeautifulSoup
import time
import os

url = 'https://www.filmweb.pl/ranking/premiere'

print('Connecting to the website...')

time.sleep(5)

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

results = soup.find(class_='page__container rankingTypeSection__container')

results_2 = soup.find(class_='page__container rankingTypeSection__container')

ratings = results_2.find_all(itemprop="ratingValue")


movies = results.find_all("h2", class_='rankingType__title')

movies_list = []
ratings_list = []

print('Connection successful.')

time.sleep(2)

os.system('clear')

for rate in ratings:
    element = rate.text.strip()
    ratings_list.append(element)

for movie in movies:
    element = movie.text.strip()
    movies_list.append(element)
    
no = 1

movies_zip = dict(zip(movies_list, ratings_list))

for k, v in movies_zip.items():
    print(f'{no}. {k} - {v}')
    no += 1
