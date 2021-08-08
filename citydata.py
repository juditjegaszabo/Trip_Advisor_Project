from bs4 import BeautifulSoup
import requests
import time


# Create BS4 object
source = requests.get('https://www.tripadvisor.co.uk/Restaurants-g186216-United_Kingdom.html').text
soup = BeautifulSoup(source, 'html.parser')


# Parse city rank
ranks = []
for rank in soup.find_all('div', attrs={'class': 'geo_rank'}):
    ranks.append(rank.text)


# Parse city name
city_list = []
for city in soup.find_all('div', attrs={'class': 'geo_name'}):
    city_list.append(city.text.split()[:-1])


# Parse city links
city_links = []
attrs = soup.find_all('div', attrs={'class': 'geo_name'})
for link in attrs:
    a = link.find('a')['href']
    full_link = f'https://www.tripadvisor.co.uk{a}'
    city_links.append(full_link)

for link in city_links:
    all_restaurants = []
    time.sleep(2)

    print(link)

    src = requests.get(link).text
    sup = BeautifulSoup(src, 'html.parser')

###########  FINDS NONE ##############
    for number in sup.find_all('div', attrs={'class': '_1D_QUaKi'}):
        all_restaurants.append(number.text)

    print(all_restaurants)
