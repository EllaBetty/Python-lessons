import requests
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
tables = soup.findAll("table", {"class": "wikitable sortable"})
target_table = tables[0]
rows = target_table.findAll("tr")
for row in rows[1:]:
    cells = row.findAll("td")
    print(cells[1].text.strip(), cells[2].text.strip(), cells[3].text.strip())

