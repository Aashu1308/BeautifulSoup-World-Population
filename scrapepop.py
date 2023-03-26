from bs4 import BeautifulSoup
import requests
from csv import writer
url = "https://www.worldometers.info/world-population/#country"
response = requests.get(url).text

soup = BeautifulSoup(response, "html.parser")
tabl = soup.find(
    'table', {'id': 'popbycountry'})
header = []
for i in tabl.find_all('th'):
    header.append(i.text)

with open("web-test/popbycountry.csv", "wt", newline='', encoding='utf-8') as f:
    csv_writer = writer(f, delimiter='|')
    csv_writer.writerow(header)
    for row in tabl.find_all('tr')[1:]:
        td = row.find_all('td')
        r = [i.text.replace('\n', '') for i in td]
        csv_writer.writerow(r)
