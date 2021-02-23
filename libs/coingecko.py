import requests


class CoinGeckoClient:
    '''Client to retrieve current crypto prices from CoinGecko'''

    BASE_URL = 'https://api.coingecko.com/api/v3'

    def get_prices(self, coins):
        URL = self.BASE_URL + '/simple/price/?vs_currencies=usd,gbp&ids='
        for coin in coins:
            URL += f'{coin},'
        prices = requests.get(URL[:-1]).json()
        return prices  # {'cardano': {'usd': 0.935098, 'gbp': 0.66278}, ...}

    def find_coin(self, symbol):
        URL = self.BASE_URL + '/coins/list'
        all_coins = requests.get(URL).json()
        for coin in all_coins:
            if coin['symbol'] == symbol:
                return coin  # {'id': 'cardano', 'symbol': 'ada', 'name': 'Cardano'}
