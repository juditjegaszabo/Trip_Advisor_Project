from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv

# Set up Chrome Driver & load webpage
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.tripadvisor.co.uk/Restaurants-g186216-United_Kingdom.html')

time.sleep(2)

# Click accept on cookie popup
privacyok = driver.find_element_by_xpath('//button[@class="evidon-banner-acceptbutton"]').click()

# Identify listing wrap on main page
cities = driver.find_elements_by_class_name('geo_wrap')

# Parse city rank
ranking = driver.find_element_by_class_name('geo_rank').text
print(ranking)

# Parse name of the city
full_city = driver.find_element_by_class_name('geo_name').text
city_name = full_city.split()[0]
print(city_name)

# Follow link to city listing all restaurants
city_link = driver.find_element_by_tag_name('div.geo_name > a').click()
#link = city_link.get_attribute('href')
print('following link')

# Total number of restaurants in the city_link
city_restaurants = driver.find_element_by_xpath('//*[@id="component_36"]/div[1]/div[1]/div[2]/span[1]/span/span').text
print(city_restaurants)

# Filter for vegan options
vegan = driver.find_element_by_xpath('//*[@id="component_48"]/div/div[9]/div[2]/div[2]/div/label/div/span/span').click()

# Ensure webpage loads fully
time.sleep(5)

# Get total number of restaurants offering vegan options
total = driver.find_element_by_xpath('//*[@id="component_36"]/div[1]/div[1]/div/span[1]/span/span').text
print(total)

# Write data to csv Filtering
with open('tripadv_data1', 'w', newline='') as f:
    fields = ['city', 'number of restaurants', 'vegan restaurants']
    thewriter = csv.DictWriter(f, fieldnames=fields)
    thewriter.writeheader()
    thewriter.writerow({'city':city_name, 'vegan restaurants':total, 'number of restaurants':city_restaurants})

print('done')
