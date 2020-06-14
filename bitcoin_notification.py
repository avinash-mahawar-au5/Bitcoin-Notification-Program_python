import requests
import time
from datetime import datetime
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import argparse

# Command line parsing
parser = argparse.ArgumentParser(description='Bitcoin Notifier')

#  Following code is for customization and passing agruments

parser.add_argument('-i', '--interval', type=float, nargs=1,
                    metavar='interval', default=[0.1], help='Time Interval in Minuits.')

parser.add_argument('-t', '--threshold', type=int, nargs=1,
                    metavar='threshold', default=[10000], help='Threshold in USD')

parser.add_argument('-c', '--currency', type=str,
                    default=['USD'], help='Currency')

args = parser.parse_args()
currency = args.currency


# URL for IFTTT weebhook

IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/hhXkyPpLFoBWtHNmG0x8tEgXdf1PJSRWiQf40jG3Hk-'


# URL for CoinMarketApi

BITCOIN_API_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '1',
    'convert': currency
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '1823bd28-f2f2-4480-bfae-eaf47d56485d',
}

session = Session()
session.headers.update(headers)

# Maximium Price
BITCOIN_PRICE_THRESHOLD = 10000


# Function for getting latest bitcoin price
def get_latest_bitcoin_price():

    response = session.get(BITCOIN_API_URL, params=parameters)

    # Convert Api resoinse to Text
    data = json.loads(response.text)

    # Fetch Price from Response
    data_float = float(data['data'][0]['quote'][currency]['price'])
    return data_float


# Function for IFTTT Post
def post_ifttt_webhook(event, value):
    data = {'value1': value}
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)

    requests.post(ifttt_event_url, json=data)


# this function combines all other fucntion accordinf to the conditions
def main():
    print(get_latest_bitcoin_price())
    print('Application is serving with time interval of ',
          args.interval[0], ' and threshold ', args.threshold[0])

# stores the respose
    bitcoin_storage = []
    while True:
        price = get_latest_bitcoin_price()
        date = datetime.now()
        bitcoin_storage.append({'date': date, 'price': price})

# Threshold condition
        if price < float(args.threshold[0]):
            post_ifttt_webhook('bitcoin_email', price)
            post_ifttt_webhook('new_updates', price)
# For regular notification
        if len(bitcoin_storage) == 1:
            post_ifttt_webhook('get_notification_bitcoin',
                               format_body(bitcoin_storage))

        if len(bitcoin_storage) == 5:
            post_ifttt_webhook(
                'bitcoin_update', format_body(bitcoin_storage))

            bitcoin_storage = []
# Specify time interval
        time.sleep(args.interval[0] * 60)

    print(get_latest_bitcoin_price())

# formate message body


def format_body(bitcoin_storage):
    rows = []
    for bitcoin_price in bitcoin_storage:
        date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')
        price = bitcoin_price['price']
        row = 'date - {}: , price- ${}'.format(date, price)
        rows.append(row)

    return '<br>'.join(rows)


if __name__ == '__main__':
    main()
