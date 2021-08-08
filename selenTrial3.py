from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


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

# Loop through the links
for link in links:
    time.sleep(3)

    driver.get(link)

    # Get total number of restaurants in the city
    all_restaurants = []
    city_restaurants = driver.find_element_by_xpath('//*[@id="component_36"]/div[1]/div[1]/div[2]/span[1]/span/span').text
    all_restaurants.append(city_restaurants)
    print(city_restaurants)

    # Filter for vegan options
    vegan = driver.find_element_by_xpath('.//*[@id="component_48"]/div/div[9]/div[2]/div[2]/div/label/div/span/span').click()

   # Wait for page to load
    time.sleep(3)

    # Get total number of restaurants offering vegan options
    vegan_restaurants = []
    filtered_result = driver.find_element_by_xpath('.//*[@id="component_36"]/div[1]/div[1]/div/span[1]/span/span').text
    vegan_restaurants.append(filtered_result)
    print(filtered_result)

    # Return to main webpage
    driver.back()

driver.quit()
