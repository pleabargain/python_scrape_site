#scrape https://www.exclusivetours.com/mauricius
# get the name of the hotels
# get the description of the hotels
import requests
from bs4 import BeautifulSoup
import csv

# get the url
url = "https://www.exclusivetours.com/mauritius"
# get the html
r = requests.get(url)
# parse the html
soup = BeautifulSoup(r.content, 'html.parser')
# get the hotels
hotels = soup.find_all('div', attrs={'class': 'hotel'})
# get the name of the hotels
hotel_names = [hotel.find('h3').text for hotel in hotels]
# get the description of the hotels
hotel_descriptions = [hotel.find('p').text for hotel in hotels]
# save the results to a csv file
with open('hotels.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'description'])
    writer.writerows(zip(hotel_names, hotel_descriptions))

# Path: python_scrape_website.py
#scrape https://www.exclusivetours.com/mauritius
# run the script
# python python_scrape_website.py