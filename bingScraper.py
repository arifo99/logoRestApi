import requests
from bs4 import BeautifulSoup

class BingScraper:

   def __init__(self):

      self.url = "https://www.bing.com/images/search"

   def getLogoLink(self, companyName):

      r = requests.get(self.url, params={
            "q": companyName + " logo"
         })
      
      pageSoup = BeautifulSoup(r.text, 'html.parser')
      
      return pageSoup.find('img', {'class': 'mimg'}).attrs['src']


