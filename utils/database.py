import sqlite3


class PortfolioClient:
    '''Client for adding/removing coins to portfolio table'''

    def create_portfolio_table(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS portfolio(id text primary key, symbol text, total real)')

        connection.commit()
        connection.close()

    def get_portfolio_data(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM portfolio')
        portfolio = [{'id': row[0], 'symbol': row[1], 'total': row[2]} for row in cursor.fetchall()]

        connection.commit()
        connection.close()
        return portfolio

    def add_coin(self, id, symbol, amount):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute(f'INSERT INTO portfolio VALUES("{id}", "{symbol}", "{amount}")')

        connection.commit()
        connection.close()

    def update_total(self, symbol, amount):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute(f'UPDATE portfolio SET total = total + {amount} WHERE "symbol" = "{symbol}"')

        connection.commit()
        connection.close()

    def remove_coin(self, symbol):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute(f'DELETE FROM portfolio WHERE symbol = "{symbol}"')

        connection.commit()
        connection.close()

    def check_holding(self, symbol):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM portfolio WHERE "symbol" = "{symbol}"')
        found = cursor.fetchone()

        connection.commit()
        connection.close()

        if found:
            return True
        else: 
            return False
