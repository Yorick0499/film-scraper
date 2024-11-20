import requests
from bs4 import BeautifulSoup
import time
import os

def new_movies_eng():
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
        

    movies_zip = dict(zip(movies_list, ratings_list))

    for k, v in movies_zip.items():
        print(f'{k} - {v}')

def new_movies_pl():
    url = 'https://www.filmweb.pl/ranking/premiere'
    print('Łączenie...')

    time.sleep(5)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find(class_='page__container rankingTypeSection__container')
    results_2 = soup.find(class_='page__container rankingTypeSection__container')

    ratings = results_2.find_all(itemprop="ratingValue")
    movies = results.find_all("h2", class_='rankingType__title')

    movies_list = []
    ratings_list = []

    print('Sukces.')

    time.sleep(2)

    os.system('clear')

    for rate in ratings:
        element = rate.text.strip()
        ratings_list.append(element)

    for movie in movies:
        element = movie.text.strip()
        movies_list.append(element)
        

    movies_zip = dict(zip(movies_list, ratings_list))

    for k, v in movies_zip.items():
        print(f'{k} - {v}')

def polish_movies_pl():
    url = 'https://www.filmweb.pl/ranking/film/country/42'
    print('Łączenie...')

    time.sleep(5)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find(class_='page__container rankingTypeSection__container')
    results_2 = soup.find(class_='page__container rankingTypeSection__container')

    ratings = results_2.find_all(itemprop="ratingValue")
    movies = results.find_all("h2", class_='rankingType__title')

    movies_list = []
    ratings_list = []

    print('Sukces.')

    time.sleep(2)

    os.system('clear')

    for rate in ratings:
        element = rate.text.strip()
        ratings_list.append(element)

    for movie in movies:
        element = movie.text.strip()
        movies_list.append(element)
        


    movies_zip = dict(zip(movies_list, ratings_list))

    for k, v in movies_zip.items():
        print(f'{k} - {v}')

def polish_movies_eng():
    url = 'https://www.filmweb.pl/ranking/film/country/42'
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
        

    movies_zip = dict(zip(movies_list, ratings_list))

    for k, v in movies_zip.items():
        print(f'{k} - {v}')

def most_awaited_eng():
    url = 'https://www.filmweb.pl/ranking/wantToSee/next12monthsWorld'
    print('Connecting to the website...')

    time.sleep(5)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find(class_='page__container rankingTypeSection__container')
    
    movies = results.find_all("h2", class_='rankingType__title')

    movies_list = []

    print('Connection successful.')

    time.sleep(2)

    os.system('clear')

    for movie in movies:
        element = movie.text.strip()
        movies_list.append(element)
    
    for i in movies_list:
        print(f'{nr}. {i}')

def most_awaited_pl():
    url = 'https://www.filmweb.pl/ranking/wantToSee/next12monthsWorld'
    print('Łączenie...')

    time.sleep(5)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find(class_='page__container rankingTypeSection__container')
    
    movies = results.find_all("h2", class_='rankingType__title')

    movies_list = []

    print('Sukces.')

    time.sleep(2)

    os.system('clear')

    for movie in movies:
        element = movie.text.strip()
        movies_list.append(element)
    
    for i in movies_list:
        print(f'{i}')



language_input = str(input("Select language(polish/english): ")).lower()
os.system('clear')
while True:
    if language_input == 'english' or language_input == 'eng' or language_input == 'e':
        print('What ranking do you want to see?')
        try:
            user_input = int(input('1: Polish\n2: New movies\n3: Most awaited\n'))
        except:
            print('\nSomething went wrong\n')
        else:
            if user_input == 2:
                os.system('clear')
                new_movies_eng()
                return_key = str(input('Enter r/q to return or exit: '))
                if return_key == 'q':
                    os.system('clear')
                    break
                elif return_key == 'r':
                    continue
            elif user_input == 1:
                os.system('clear')
                polish_movies_eng()
                return_key = str(input('Enter r/q to return or exit: '))
                if return_key == 'q':
                    os.system('clear')
                    break
                elif return_key == 'r':
                    continue
            elif user_input == 3:
                os.system('clear')
                most_awaited_eng()
                return_key = str(input('Enter r/q to return or exit: '))
                if return_key == 'q':
                    os.system('clear')
                    break
                elif return_key == 'r':
                    continue
    elif language_input == 'polish' or language_input == 'pl' or language_input == 'p':
        print('Jaki ranking chcesz zobaczyć?')
        try:
            user_input = int(input('1: Polskie\n2: Nowości\n3: Najbardziej wyczekiwane\n')) 
        except:
            print('\nCoś poszło nie tak\n')
        else:
            if user_input == 2:
                os.system('clear')
                new_movies_pl()
                return_key = str(input('Wprowadź r/q, aby wrócić lub wyjść: '))
                if return_key == 'q':
                    os.system('clear')
                    break
                elif return_key == 'r':
                    os.system('clear')
                    continue
            elif user_input == 1:
                os.system('clear')
                polish_movies_pl()
                return_key = str(input('Wprowadź r/q, aby wrócić lub wyjść: '))
                if return_key == 'q':
                    os.system('clear')
                    break
                elif return_key == 'r':
                    continue
            elif user_input == 3:
                os.system('clear')
                most_awaited_pl()
                return_key = str(input('Wprowadź r/q, aby wrócić lub wyjść: '))
                if return_key == 'q':
                    os.system('clear')
                    break
                elif return_key == 'r':
                    continue
            else:
                continue
