from bs4 import BeautifulSoup
from newspaper import Article
import requests
import json
import pandas
from DataBaseConnection import add
from datetime import date
from DataBaseConnection import add
import concurrent.futures

pickle=pandas.read_pickle('symbols.pickle')
curdate=date.today()

def NewsArticlesReuter(security):

    source=requests.get('https://www.reuters.com/companies/{}'.format(security)).text
    soup=BeautifulSoup(source,'lxml')

    for mainpart in soup.find_all('a',class_="TextLabel__text-label___3oCVw TextLabel__black-to-orange___23uc0 TextLabel__medium___t9PWg MarketStoryItem-headline-2cgfz"):
        url=mainpart['href']
        try:
            art = Article(url)
            art.download()
            art.parse()
            art.nlp()

            hash_mera = {
                'security':security,
                'Current_Date':f'{curdate}',
                'authors': art.authors,
                'publish_date': art.publish_date,
                'body': art.summary,
                'title': art.title,
                'Source':'Reuters',
                'Category':'News',
                'Topics':art.keywords
            }
            add(hash_mera)
        except:
            print("excluded")
            continue

# if __name__ == "__main__":
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#      executor.map(NewsArticlesReuter,pickle.symbol)
#     pass