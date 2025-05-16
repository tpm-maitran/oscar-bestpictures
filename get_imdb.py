import requests
from bs4 import BeautifulSoup as bs

def get_imdb(imdb_id, headers):

    url = f'https://www.imdb.com/title/{imdb_id}/reference'  # link to the imdb page of a film
    response = requests.get(url, headers=headers)
    soup = bs(response.text, 'html.parser')
    
    # release year
    try:
        release_year = soup.find('span', class_='titlereference-title-year').find('a').text.strip()
    except:
        release_year = ''
    
    # film rating
    try:
        rated = soup.find('ul', class_='ipl-inline-list').find('li').text.strip()
    except:
        rated = ''
        
    # budget
    try:
        budget = soup.find('td', string='Budget').find_next_sibling('td').text.strip().split()[0]
    except:
        budget = ''
        
    #language
    try:
        language = soup.find('td', string='Language').find_next_sibling('td').find('a').text.strip()
    except:
        language = ''
    
    # imdb rating
    try:
        imdb_rating = soup.find('span', class_='ipl-rating-star__rating').text.strip()
    except:
        imdb_rating = ''
    
    # number of imdb votes
    try:
        imdb_votes = soup.find('span', class_='ipl-rating-star__total-votes').text.strip('()')
    except:
        imdb_votes = ''
        
    return release_year, rated, budget, language, imdb_rating, imdb_votes