import requests
import time

# Your CoinMarketCap API key
api_key = 'dabcde74-0f9e-4f07-be8e-c16ccd7d3a9b'

# The URL for the CoinMarketCap API
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# The parameters for the API call
parameters = {
    'start': '1',  # The starting point (rank) of the cryptocurrencies to return
    'limit': '10',  # The number of cryptocurrencies to return
    'convert': 'USD'  # The fiat currency to convert to
}

# The headers for the API call
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key
}

# The target price for notification
target_price = 50000  # Example target price in USD

def fetch_prices():
    try:
        response = requests.get(url, headers=headers, params=parameters)
        data = response.json()
        return data['data']
    except Exception as e:
        print(f'Error fetching data: {e}')
        return None

def check_price(cryptocurrencies, target_price):
    for crypto in cryptocurrencies:
        if crypto['name'] == 'Bitcoin':  # Replace 'Bitcoin' with your desired cryptocurrency
            price = crypto['quote']['USD']['price']
            print(f"Current price of Bitcoin: ${price}")
            if price >= target_price:
                print(f'Bitcoin has reached the target price of ${target_price}!')
                return True
    return False

while True:
    cryptocurrencies = fetch_prices()
    if cryptocurrencies and check_price(cryptocurrencies, target_price):
        break
    time.sleep(60)  # Wait for 1 minute before checking again
import requests
import pandas as pd

def list_coins():
    url = "https://api.coincap.io/v2/assets"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        coins = data.get('data', [])

        # Create a DataFrame
        coins_df = pd.DataFrame(coins, columns=['rank', 'name', 'symbol', 'priceUsd', 'marketCapUsd', 'volumeUsd24Hr'])

        # Display the DataFrame
        print(coins_df)
    else:
        print("Failed to retrieve data")

if __name__ == "__main__":
    list_coins()