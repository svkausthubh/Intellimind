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

def NewsArticlesTimes(security):

    source=requests.get('https://timesofindia.indiatimes.com/topic/{}/news'.format(security)).text
    soup=BeautifulSoup(source,'lxml')

    for mainpart in soup.find_all('div',class_="content"):
        laddu=mainpart.find('a')['href']
        url=f'https://timesofindia.indiatimes.com/{laddu}'
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
                'Source':'TimesOfIndia',
                'Category':'News',
                'Topics':art.keywords
            }
            add(hash_mera)
        except:
            print("excluded")
            continue

# if __name__ == "__main__":
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#      executor.map(NewsArticlesTimes,pickle.symbol)
#     pass