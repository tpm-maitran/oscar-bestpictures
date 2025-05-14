#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup as bs
import re

def get_rt(url, headers):
    
    response = requests.get(url, headers=headers)
    soup = bs(response.text, 'html.parser')
    
    release_year = ''
    rt_score = ''
    rt_votes = ''
    audience_score = ''
    audience_votes = ''   
    
    if response.status_code == 200:
        
        # release year
        try:
            label = soup.find('rt-text', attrs={'data-qa': 'item-label', 'class': 'key'}, string=lambda s: s and 'Release Date' in s)
            release_year = label.find_next('rt-text', attrs={'data-qa': 'item-value'}).text.split(',')[1].strip()
        except:
            release_year = ''
        
        
        table = soup.find_all('div', class_='media-scorecard no-border')
        
        for r in table:
            
            # tomato score (tomatometer)
            try:
                rt_score = r.find('rt-text', slot='criticsScore').text.strip('%')
            except:
                rt_score = ''
            
            # number of critic votes
            try:
                rt_votes = re.search(r'\d+', r.find('rt-link', slot='criticsReviews').text).group()
            except:
                rt_votes = ''
            
            # audience score (popcornmeter)
            try:
                audience_score = r.find('rt-text', slot='audienceScore').text.strip('%')
            except:
                audience_score = ''
                
            # number of audience votes
            try:
                audience_votes = re.search(r'\d[\d,]*\+?', r.find('rt-link', slot='audienceReviews').text).group()
            except:
                audience_votes = ''
                
    return release_year, rt_score, rt_votes, audience_score, audience_votes

