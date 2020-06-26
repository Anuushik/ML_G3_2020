import logging
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

from storage import Persistor

logger = logging.getLogger(__name__)


class Scraper:

        def __init__(self):
            self.persistor = Persistor()

        def scrape(self):
            #Gives the text from zigzag website

            url = 'https://www.zigzag.am/am/tv-audio-video/tvs.html'
        # opening the page and taking the data
            data = uReq(url)
            page_html = data.read()
      #     response = requests.get(url)
            data.close()
        # #html parsing
        #     page_soup = BeautifulSoup(page_html, "html.parser")
        #   #  print(page_soup.body)
        #     #for each product
        #     categories = page_soup.findAll("div", {"class":"item_category"})
        #     print(category[0])

        #     for category in categories:
        #         item = category.a["item_name item_link"]
        #         title = category.findAll("a", {"class":"item_name"})
        #         name = title[0].text

        #         print("item: ", item)
        #         print ("title: ", title )
        #         print("name: ", name)

            self.persistor.save_raw_data(page_html, "tvs.html")

        #   '''   if not response.ok:
                    # log the error
            #        logger.error(response.text)

            #    else:
                    # Note: here json can be used as response.json
            #      data = response.text

                    # save scraped objects here
                    # you can save url to identify already scrapped objects
                    # filename = title + '.html'
                    # self.storage.save_raw_data(data, filename)

scraper =Scraper()
scraper.scrape()
