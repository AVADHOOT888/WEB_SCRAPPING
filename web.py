import requests
import pandas as pd
from bs4 import BeautifulSoup

page=requests.get("https://forecast.weather.gov/MapClick.php?lat=34.053570000000036&lon=-118.24544999999995#.YRigb4gzbIU")

soup=BeautifulSoup(page.content,'html.parser')

# print(soup.find_all('a'))

week=soup.find(id='seven-day-forecast-body')

items=week.find_all(class_='tombstone-container')

# print(items[0].find(class_='period-name').get_text())
# print(items[0].find(class_='short-desc').get_text())
# print(items[0].find(class_='temp').get_text())

period_names=[item.find(class_='period-name').get_text() for item in items]
# print(period_names)
short_descriptions=[item.find(class_='short-desc').get_text() for item in items]
# print(short_descriptions)
temperatures=[item.find(class_='temp').get_text() for item in items]
# print(temperatures)


weather_stuff=pd.DataFrame({'period':period_names,'short-description':short_descriptions,'temperature':temperatures})

print(weather_stuff)

weather_stuff.to_csv('weather.csv')
