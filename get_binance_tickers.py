#! /usr/bin/env python
import bs4 as bs
import requests
import pickle


def save_ticker_pairs():
    cmc_binance_url = 'https://coinmarketcap.com/exchanges/binance/'
    response = requests.get(cmc_binance_url)
    if response.ok:
        soup = bs.BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'id': 'exchange-markets'})
        ticker_pairs = []

        for row in table.findAll('tr')[1:]:
            ticker_pair = row.findAll('td')[2].text
            ticker_pairs.append(ticker_pair.strip().replace('/', ''))

    with open('binance_ticker_pairs.pickle', 'wb') as f:
        pickle.dump(ticker_pairs, f)


if __name__ == '__main__':
    save_ticker_pairs()
