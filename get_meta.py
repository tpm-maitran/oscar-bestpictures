import requests
from bs4 import BeautifulSoup as bs
import re

def get_meta(url, headers):
    
    response = requests.get(url, headers=headers)
    
    metascore = ''
    meta_votes = ''
    release_year = ''
    
    if response.status_code == 200:
        soup = bs(response.text, 'html.parser')
        
        # metascore
        try:
            metascore = soup.find('span', {'data-v-e408cafe': True}).text.strip()
        except:
            metascore = ''

        # number critic votes
        try:
            meta_votes = re.search(r'\d+', soup.find('a', class_='c-ScoreCard_reviewLink').text).group(0)
        except:
            meta_votes = ''
       
        # release year
        try:
            block = soup.find('div', attrs={'data-testid': 'hero-metadata', 'class': 'c-heroMetadata'})
            release_year = block.find('span').text.strip()
        except:
            release_year = ''
            
    return metascore, meta_votes, release_year
