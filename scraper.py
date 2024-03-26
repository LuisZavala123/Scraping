from bs4 import BeautifulSoup
import requests
import datetime
import csv
import pandas as pd
from os.path import exists

headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0",
          "Accept-Encoding": "gzip, deflate, br",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
          "DNT": "1",
          "Connection" : "close",
          "Upgrade-Insecure-Requests": "1",}


def check_price(URL):

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content,"html.parser")

    soup1 = BeautifulSoup(soup1.prettify(),"html.parser")

    title= soup1.find(id='productTitle').get_text()
    price= soup1.find_all('span', class_='a-price aok-align-center reinventPricePriceToPayMargin priceToPay', limit=1)[0].get_text()
    title= title.strip()
    price= price.replace("\n","")
    price= price.replace(" ","")
    price= price.strip()[1:]

    today = datetime.date.today()

    header = ['Title','Price','Date']
    data = [title,price,today]

    if (exists(f'ScraperDataset.csv')):
        with open('ScraperDataset.csv', 'a+', newline='', encoding='UTF8') as Dset:
            writer = csv.writer(Dset)
            writer.writerow(data)
    else:
        with open('ScraperDataset.csv', 'w', newline='', encoding='UTF8') as Dset:
            writer = csv.writer(Dset)
            writer.writerow(header)
            writer.writerow(data)

check_price('https://www.amazon.com.mx/Acteck-Monitor-Altavoces-Captive-SP240/dp/B09YS943Q1/ref=sr_1_2?crid=3UWE0F9GEDT0L&dib=eyJ2IjoiMSJ9.5Dv_5BKQS5_1m0muzBDqVrbJqbBvF_BKhp8qpE-7TxsZOka9-d4u80NQZ2r1tteUrALQltKSPN-QL2xltNsLWdT3eR4kk8pQWeWh78sFyvBfJK81il4PkD11C1G-ukMlp5ttteAuy8iNNT4JpKUxSKK7Rt2iFtc880O6cVfR9KbrERyjdhH_-ewVOJx7eyM7280r6ZMZVqwnLhHN57bbfGfrLebE3hwnLmBZuXxlogYnIvqo69_HwnT99Ek8oagnuldpzdtQfPIzi2MVSYxcip8DFLTROYO4zOhEVkef1rA.qFW2jJdOOlXe2t2IpV8FThAE3WHaedt6QsXTBrJJic0&dib_tag=se&keywords=monitor&qid=1711396681&sprefix=moni%2Caps%2C146&sr=8-2&ufe=app_do%3Aamzn1.fos.4e545b5e-1d45-498b-8193-a253464ffa47')

readset = pd.read_csv(r'ScraperDataset.csv')
print(readset)

