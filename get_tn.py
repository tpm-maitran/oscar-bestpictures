import requests
from bs4 import BeautifulSoup as bs

def get_tn(url, headers):
    response = requests.get(url, headers=headers)

    domestic = ''
    international = ''
    worldwide = ''
    genre = ''
    studio = ''
    country = ''
    runtime = ''
    release_year = ''

    if response.status_code == 200:
        soup = bs(response.text, 'html.parser')

        # box office
        table = soup.find('table', id='movie_finances')
        
        if table:
            
            fin = table.find_all('tr')

            try:
                domestic = next(r.find_all('td')[1].text.strip() for r in fin if 'Domestic Box Office' in r.text)
            except:
                domestic = ''

            try:
                international = next(r.find_all('td')[1].text.strip() for r in fin if 'International Box Office' in r.text)
            except:
                international = ''

            try:
                worldwide = next(r.find_all('td')[1].text.strip() for r in fin if 'Worldwide Box Office' in r.text)
            except:
                worldwide = ''

        # genre
        try:
            b_tag = soup.find('b', string=lambda s: s and s.strip() == 'Genre:')
            genre = b_tag.find_next('td').text.strip()
        except:
            genre = ''

        # studio
        try:
            b_tag = soup.find('b', string=lambda s: s and s.strip() == 'Domestic Releases:')
            studio = b_tag.find_next('td').find('a').text.strip()
        except:
            studio = ''

        # production country
        try:
            b_tag = soup.find('b', string=lambda s: s and s.strip() == 'Production Countries:')
            country = b_tag.find_next('td').text.strip()
        except:
            country = ''

        # runtime
        try:
            b_tag = soup.find('b', string=lambda s: s and s.strip() == 'Running Time:')
            runtime = b_tag.find_next('td').text.strip()
        except:
            runtime = ''
            
        # release year
        try:
            release_year = soup.find('h1').text.split('(')[-1].strip(')')
        except:
            release_year = ''

    return domestic, international, worldwide, genre, studio, country, runtime, release_year