import json
import requests
from datetime import datetime
from decouple import config
# Replace with your actual CoinMarketCap API key
api_key = config = ('COIN_API_KEY ')
currency = 'KES'
global_url = f'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest?convert={currency}'
# Define headers including the API key
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
}
# Make the request
response = requests.get(global_url, headers=headers)
# Check if the response was successful
if response.status_code == 200:
    results = response.json()
    try:
        active_cryptocurrencies = results['data']['active_cryptocurrencies']
        active_markets = results['data']['active_exchanges']
        bitcoin_percentage = results['data']['btc_dominance']
        last_updated = results['status']['timestamp']
        global_cap = results['data']['quote'][currency]['total_market_cap']
        global_volume = results['data']['quote'][currency]['total_volume_24h']
        # Format the numbers with commas
        active_cryptocurrencies_string = '{:,}'.format(active_cryptocurrencies)
        active_markets_string = '{:,}'.format(active_markets)
        global_cap_string = '{:,}'.format(int(global_cap))
        global_volume_string = '{:,}'.format(int(global_volume))
        # Format the last updated time
        last_updated_string = datetime.strptime(last_updated, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%B %d, %Y at %I:%M %p')
        print()
        print(f'There are currently {active_cryptocurrencies_string} active cryptocurrencies and {active_markets_string} active markets.')
        print(f'The global cap of all cryptos is {global_cap_string} KES and 24h global volume is {global_volume_string} KES.')
        print(f'Bitcoin\'s total percentage of the global cap is {bitcoin_percentage}%.')
        print()
        print(f'This information was updated on {last_updated_string}.')
    except KeyError as e:
        print(f'Error: Missing key in response data - {e}')
else:
    print(f'Failed to retrieve data: {response.status_code} - {response.text}')