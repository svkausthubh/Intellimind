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

def NewsArcticlesYahoo(security):

    source=requests.get('https://in.finance.yahoo.com/quote/{}'.format(security)).text
    soup=BeautifulSoup(source,'lxml')

    for mainpart in soup.find_all('a',class_="Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled"):
        laddu=mainpart['href']
        url=f'https://in.finance.yahoo.com{laddu}'
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
                'Source':'Yahoo.com',
                'Category':'News',
                'Topics':art.keywords
            }
            add(hash_mera)
        except:
            print("excluded")
            continue


