from bs4 import BeautifulSoup
import requests
import time
import csv
import urllib.request

####### WON'T RETRIEVE ########
response = urllib.request.urlopen('https://www.tripadvisor.co.uk/Restaurants-g186216-United_Kingdom.html')
html = response.read()
# Go to URL and create BS4 object
soup = BeautifulSoup(html, 'lxml')

print('got soup')

with open('city_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Parse city rank
    for rank in soup.find_all('div', attrs={'class': 'geo_rank'}):
        writer.writerow([rank])

    # Parse city name
    for city in soup.find_all('div', attrs={'class': 'geo_name'}):
        writer.writerow([city.text.split()[:-1]])

    # Parse city links
    attrs = soup.find_all('div', attrs={'class': 'geo_name'})
    for link in attrs:
        a = link.find('a')['href']
        full_link = f'https://www.tripadvisor.co.uk{a}'
        writer.writerow([full_link])

print('Open city_data.csv for results.')
