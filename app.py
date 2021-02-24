from libs.coingecko import CoinGeckoClient
from utils.database import PortfolioClient


USER_MENU = '''\nPlease choose one of the following:
- 'v' to display your portfolio
- 'a' to add a new coin to your portfolio
- 'u' to increase/decrease coins from your portfolio
- 'd' to delete a coin from your portfolio
- 'q' to exit

Input your choice here: '''

portfolio = PortfolioClient()
coingecko = CoinGeckoClient()

portfolio.create_portfolio_table()


def display_portfolio():
    coins = portfolio.get_portfolio_data()  # [{'id': 'cardano', 'symbol': 'ada', 'total': 500}, ...]
    if coins:
        ids = [coin['id'] for coin in coins]
        prices = coingecko.get_prices(ids)  # {'cardano': {'usd': 0.935098, 'gbp': 0.66278}, ...}
        for coin in coins:
            coin['price'] = prices[coin['id']]
            coin['fiat_total'] = {fiat: coin['total'] * coin['price'][fiat] for fiat in coin['price']}
        print(coins)
    else:
        print('Your portfolio is currently empty.')


def new_coin():
    symbol = input('Please provide ticker for coin: ')
    coin = coingecko.find_coin(symbol)  # {'id': 'cardano', 'symbol': 'ada', 'name': 'Cardano'}
    if coin:
        amount = input('Please provide initial amount: ')
        portfolio.add_coin(coin['id'], coin['symbol'], amount)
        print('Coin added successfully.')
    else: 
        print('Sorry, that coin is not available on CoinGecko, please try again.')


def add_to_existing():
    symbol = input('Please provide ticker for coin: ')
    if portfolio.check_holding(symbol):
        amount = float(input('How many coins would you like to add? '))
        portfolio.update_total(symbol, amount)
        print('Update successful.')
    else: 
        print('Sorry, that coin is not currently in your portfolio. Please try again.')


def delete_coin():
    symbol = input("Please provide ticker for coin: ")
    if portfolio.check_holding(symbol):
        sure = input('Are you sure you wish to remove this coin? (y/n) ')
        while sure != 'n':
            if sure == 'y':
                portfolio.remove_coin(symbol)
                print("Coin removed successfully.")
                break
            else:
                print('Please choose a valid option.')
            sure = input('Are you sure you wish to remove this coin? (y/n) ')
    else: 
        print('Sorry, that coin is not currently in your portfolio. Please try again.')
            

user_options = {
    'v': display_portfolio,
    'a': new_coin,
    'u': add_to_existing,
    'd': delete_coin
}


def menu():
    user_input = input(USER_MENU)

    while user_input != 'q':
        if user_input in user_options:
            user_options[user_input]()
        else: 
            print('Please chooses a valid option')
        
        user_input = input(USER_MENU)


menu()
