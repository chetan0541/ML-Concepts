from requests import get
from bs4 import BeautifulSoup
import pandas as pd 

url = 'https://www.imdb.com/search/title/?release_date=2017&sort=num_votes,desc&page=1'
response = get(url, headers= {"Accepted-Language":"en-US"})
# print(response.text[:20299])

#object initialization 
hsoup = BeautifulSoup(response.text,'html.parser')
#getting the relevant containers(tags)
movie_containers = hsoup.find_all(name='div', class_ = 'lister-item mode-advanced')

#storing the 0th index i.e the 1st movie
first_movie_logan = movie_containers[0]
#extracting data
first_name = first_movie_logan.h3.a.text
first_year = first_movie_logan.h3.find(name='span', class_= 'lister-item-year text-muted unbold')
first_year = first_year.text
first_rating = first_movie_logan.find(name='strong')
first_meta_score = first_movie_logan.find(name='span', attrs={'class':'metascore favorable'})
first_meta_score = first_meta_score.text
# first_meta_score = first_meta_score
print(first_meta_score)

names = []
years = []
ratings = []
meta_score = []

for container in movie_containers:
    if container.find(name='span', attrs={'class':'metascore favorable'}) is not None:
        name = container.h3.a.text
        names.append(name)
        
        year = container.h3.find(name='span', attrs={'class':'lister-item-year text-muted unbold'}).text
        years.append(year)

        rating = float(container.strong.text)
        ratings.append(rating)

        m_score = container.find(name='span', attrs={'class':'metascore favorable'}).text
        meta_score.append(m_score)

movies_2017 = pd.DataFrame({
    'Movie Name':names,
    'Year':years,
    'Ratings':ratings,
    'Meta Score':meta_score
}
)
# print(movies_2017)

#saving the data in a csv file
movies_2017.to_csv('Movies.csv',encoding='utf-8')