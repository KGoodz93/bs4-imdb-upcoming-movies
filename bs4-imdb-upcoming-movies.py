"""
Author: Kelvin Gooding
Created: 08/06/2022
Version: 1.000
"""

# Modules

from bs4 import BeautifulSoup
import requests
import datetime
import csv

# Variables

dateformat1 = datetime.datetime.today().strftime("%Y-%m")
dateformat2 = datetime.datetime.today().strftime("%B %Y")
url = f"https://www.imdb.com/movies-coming-soon/{dateformat1}"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

with open(f"imdb-upcoming-movies-{dateformat1}.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Length', 'Description'])

    # Script

    print(f"IMDB - Upcoming movie releasing in {dateformat2}. {url}\n")

    match = soup.find_all('td', attrs={'class': 'overview-top'})

    for item in match:
        headline = item.h4.a.text
        summary = item.find('div', attrs={'class': 'outline'}).text
        length = item.p.time.text
        writer.writerow([f"{headline.strip()}", f"{length}", f"{summary.strip()}"])
