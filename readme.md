# Which UK cities are the most vegan friendly?


## The Data

I built a [web scraper](https://github.com/juditjegaszabo/Trip_Advisor_Project/blob/main/selenium_webparser.py) using Selenium to interact with Trip Advisor's dynamic website. [This page](https://www.tripadvisor.co.uk/Restaurants-g186216-United_Kingdom.html), listing the 20 most popular cities in the UK, was my starting point. I followed each link and pulled the total number of restaurants, set the filter to only show restaurants offering vegan option, then parsed the number of the filtered search results as well. All this was saved into a [csv file](https://github.com/juditjegaszabo/Trip_Advisor_Project/blob/main/rest_data.csv).

I also needed recent population data for these cities. The [figures](https://github.com/juditjegaszabo/Trip_Advisor_Project/blob/main/populationdata.csv) were downloaded from [here](https://worldpopulationreview.com/countries/cities/united-kingdom).

## The Analysis

Before I could start the [analysis](https://github.com/juditjegaszabo/Trip_Advisor_Project/blob/main/analysis.ipynb), I had to clean the csv file containing the parsed web data. I loaded everything into Pandas using Jupyter Notebook, focusing on ensuring data integrity and smooth processing.

## The Methodology

I first wanted to see how widespread veganism is, as reflected by the number of restaurants offering this option on their menu. Surely, a higher number of such restaurants in a city would suggest that there is a demand for this dietary option. Also interested in finding out if there was a correlation between the size of the city and the number of restaurants with a vegan menu, I analysed data on population of the 20 cities in question as well.

## The Result

Surprisingly or not, the best city for vegans is not London. The size of the population and the status of the capital as a cultural hub would indeed suggest that it must have enbraced the vegan movement ahead of other parts of the country, but that is not so. In fact, London (and other major cities such as Birmingham) are at the very end of the list, indicating that from a vegan standpoing, London is not the centre of the world.

Brighton, the city with the smallest population, offers by far the greatest number of restaurants that cater for vegans in the UK. The seaside resort is famous for many things, like it's pier and nightlife, and now we can add "Vegan Capital" to the list as well.

Looking at the finalists, the 10 best cities for vegans, I noticed that a number of them (6 out of 10) are located in the North. The reason for this would be interesting to look into and investigate further.
