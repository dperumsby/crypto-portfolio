import sqlite3


class PortfolioClient:
    '''Client for adding/removing coins to portfolio table'''

    def create_portfolio_table(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS portfolio(coin text primary key, total real)')

        connection.commit()
        connection.close()

    def get_portfolio_data(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM portfolio')
        portfolio = [{'Coin': row[0], 'Total': row[1]} for row in cursor.fetchall()]

        connection.commit()
        connection.close()
        return portfolio

    def add_coin(self, coin, amount):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute(f'INSERT INTO portfolio VALUES("{coin}", "{amount}")')

        connection.commit()
        connection.close()

    def update_total(self, coin, amount):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute(f'UPDATE portfolio SET total = total + {amount} WHERE "coin" = "{coin}"')

        connection.commit()
        connection.close()

    def remove_coin(self, coin):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute(f'DELETE FROM portfolio WHERE coin = "{coin}"')

        connection.commit()
        connection.close()

    def check_holding(self, coin):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM portfolio WHERE "coin" = "{coin}"')
        found = cursor.fetchone()

        connection.commit()
        connection.close()

        if found:
            return True
        else: 
            return False
