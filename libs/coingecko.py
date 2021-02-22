import requests


class CoinGeckoClient:
    '''Client to retrieve current crypto prices from CoinGecko'''

    BASE_URL = 'https://api.coingecko.com/api/v3'

    def __init__(self):
        pass

    def update(self):
        pass

    def check(self, coin):
        URL = self.BASE_URL + '/coins/list'
        all_coins = requests.get(URL).json()
        for c in all_coins:
            if c['symbol'] == coin:
                return True


