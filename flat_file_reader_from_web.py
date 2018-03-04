'''pull flatfile from web'''

from urllib.request import urlretrieve

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'

urlretrieve(url, 'winequality-white.csv')



# '''Webscrape Data'''
# from urllib.request import urlopen, Request
# url = "https://www.wikipedia.org/"
# request = Request(url)
# response = urlopen(request)
# html = response.read()
# response.close()

'''Webscrape made easier'''
# import requests
# url = "https://www.wikipedia.org/"
# r = requests.get(url)
# text = r.text()
# print(text)

'''Webscrape and parse'''
from bs4 import BeautifulSoup
import requests
url = 'https://www.crummy.com/software/BeautifulSoup'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)
# print(soup.prettify())
# print(soup.title)
# print(soup.get_text())
for link in soup.find_all('a'):  # print all hyperlinks
    print(link.get('href'))
