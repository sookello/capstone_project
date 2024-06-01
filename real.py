import requests

def fetch_price(bitcoin):
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=' + bitcoin + '&vs_currencies=usd'
    response = requests.get(url)
    price_data = response.json()
    return price_data[bitcoin]['usd']

import pandas as pd

crypto_data = {'Name': [], 'Price': []}

def add_to_dataframe(name, price):
    crypto_data['Name'].append(name)
    crypto_data['Price'].append(price)
    df = pd.DataFrame(crypto_data)
    print(df)

import matplotlib.pyplot as plt

def plot_prices(df):
    df.plot(kind='bar', x='Name', y='Price')
    plt.xlabel('Cryptocurrency')
    plt.ylabel('USD Price')
    plt.title('Cryptocurrency Prices')
    plt.show()