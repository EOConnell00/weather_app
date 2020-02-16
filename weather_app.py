import requests
from bs4 import BeautifulSoup

URL = 'https://www.theweathernetwork.com/ca/weather/new-brunswick/fredericton'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='today_tomorrow_nitro')

print(results)
#temp = soup.find('div', class_='fx_card tonigth')
#print(temp.prettify())