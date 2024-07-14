import requests
import time
from plyer import notification
from prettytable import PrettyTable
# Replace with your CoinMarketCap API key
API_KEY = 'dabcde74-0f9e-4f07-be8e-c16ccd7d3a9b'
# URL for the CoinMarketCap API
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

# Function to get cryptocurrency price


def get_crypto_price(symbol):
    parameters = {
        'symbol': symbol,
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY,
    }
    response = requests.get(URL, headers=headers, params=parameters)
    data = response.json()
    return data['data'][symbol]['quote']['USD']['price']

# Function to send notification


def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Crypto Price Notifier',
        timeout=10  # Notification will disappear after 10 seconds
    )


# Set your cryptocurrency and threshold price here
CRYPTO_SYMBOL = 'BTC'
PRICE_THRESHOLD = 30000  # Set your desired price threshold

while True:
    try:
        price = get_crypto_price(CRYPTO_SYMBOL)
        print(f'The current price of {CRYPTO_SYMBOL} is ${price:.2f}')
        if price > PRICE_THRESHOLD:
            send_notification(f'{CRYPTO_SYMBOL} Price Alert', f'The price of {
                              CRYPTO_SYMBOL} has crossed ${PRICE_THRESHOLD}. Current price: ${price:.2f}')
        time.sleep(300)  # Check price every 5 minutes
    except Exception as e:
        print(f'An error occurred: {e}')
        time.sleep(60)  # Wait for 1 minute before trying again
