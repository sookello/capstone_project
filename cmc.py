import requests
import pandas as pd
from IPython.display import display, clear_output
import time

# Your CoinMarketCap API key
API_KEY = 'dabcde74-0f9e-4f07-be8e-c16ccd7d3a9b'

# URL for the CoinMarketCap API
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# Parameters for the API request
parameters = {
    'start': '1',
    'limit': '100',
    'convert': 'USD'
}

# Headers for the API request
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}


def fetch_data():
    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()
    return data['data']


def process_data(data):
    df = pd.DataFrame(data)
    df['percent_change_24h'] = df['quote'].apply(
        lambda x: x['USD']['percent_change_24h'])
    df['market_cap'] = df['quote'].apply(lambda x: x['USD']['market_cap'])
    df = df[['name', 'symbol', 'market_cap', 'percent_change_24h']]
    return df


def display_tables(df):
    top_5 = df.nlargest(5, 'market_cap')
    bottom_5 = df.nsmallest(5, 'market_cap')

    clear_output(wait=True)

    print("Top 5 Cryptocurrencies by Market Cap:")
    display(top_5)

    print("\nBottom 5 Cryptocurrencies by Market Cap:")
    display(bottom_5)


def main():
    while True:
        data = fetch_data()
        df = process_data(data)
        display_tables(df)
        time.sleep(60)


if __name__ == "__main__":
    main()
