from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import csv


# Set up Chrome Driver & load webpage
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.tripadvisor.co.uk/Restaurants-g186216-United_Kingdom.html')

# Give time for cookie window to pop up
elems = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH, '//button[@class="evidon-banner-acceptbutton"]')))

# Click accept on cookie popup
privacyok = driver.find_element_by_xpath('//button[@class="evidon-banner-acceptbutton"]').click()

# Identify listing wraps on main page, get their link & add them to list
cities = driver.find_elements_by_css_selector(".geo_name [href]")
links = [city.get_attribute('href') for city in cities]

# Open CSV Writer and create csv file
with open('rest_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    all_res = []
    veg_res = []

    # Parse all city ranks
    ranking = []
    for rank in driver.find_elements_by_class_name("geo_rank"):
        ranking.append([rank.text])

    # Parse all city names
    cities = []
    for city in driver.find_elements_by_class_name("geo_name"):
        cities.append(city.text.split()[:-1])

    # Loop through the links
    for link in links:
        time.sleep(1)

        driver.get(link)

        # Get total number of restaurants in the city
        for res in driver.find_elements_by_xpath('//*[@id="component_36"]/div[1]/div[1]/div[2]/span[1]/span/span'):
            all_res.append([res.text])

        # Filter for vegan options
        vegan = driver.find_element_by_xpath('.//*[@id="component_48"]/div/div[9]/div[2]/div[2]/div/label/div/span/span').click()

        # Wait for page to load
        time.sleep(3)

        # Get total number of restaurants offering vegan options
        for veg in driver.find_elements_by_xpath('.//*[@id="component_36"]/div[1]/div[1]/div/span[1]/span/span'):
            veg_res.append([veg.text])

        # Return to main webpage
        driver.back()

    # Write data to file
    writer.writerows(zip(ranking, cities, all_res, veg_res))

# Close webdriver 
driver.quit()

print('Open rest_data.csv for results.')
