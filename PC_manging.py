import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
page = urlopen('https://market.yandex.ru/search?cvredirect=2&text=pc&suggest_reqid=28568894661294203032579100827647')
soup = BeautifulSoup(page, "html5lib")
prices = soup.findAll('div', attrs={"class":"price"})
import re
prices = [att.text for att in prices]
print(prices)
prices = [re.search(r'(\d*\s\d*)', line) for line in prices]
print(prices)