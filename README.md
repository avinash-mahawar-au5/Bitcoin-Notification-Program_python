# Bitcoin Notifications

This program fetch the current price of bitcoin from an API and serve the notifications as per our needs. This project includes the Regular notifications and an Emergency notification when the price of Bitcoin falls below the Threshold Price that we have given as a standard paramater.

##  Getting Started


## Prerequisites

1: Install python environment [Python3](https://www.python.org/downloads/release/python-383/).

2: Get a [CoinMarketCap](https://pro.coinmarketcap.com/signup/) API key.

3: Need to have a basic understanding of how POST and GET call works in Python. [Learn](https://www.geeksforgeeks.org/get-post-requests-using-python/).


## Installing 

If you find the prerequisties section getting tough to implement. No worries we will do it together now.

```shell
$ mkvirtualenv -p $(which python3) bitcoin_notifications
```
```shell
$ workon bitcoin_notifications
$ pip install requests==2.18.
```

## Building the program

### Fetching the Bitcoin Price

First, we have to import the requests module and define the bitcoin_api_url variable which contains the Coinmarketcap API URL for Bitcoin.

```python
import requests from Requests,Session
BITCOIN_API_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest/'
```

Now Send the HTTP GET request and save the respoonse. Since the API return the JSON response we have to convert it to the python object by calling .json() function.

```python
response = session.get(BITCOIN_API_URL,params=parameters)
return data=json.loads(response.text)
```

Now before we move further lets make some IFTTT Applets.

## Creating IFTTT Applets

Now this is the important and main part of this application. We need to create two new IFTTT applets: one for emergency Bitcoin price notifications and one for regular updates.

In this project we are going to make below Applets
1.For send an Email for Emergency notification.

2.For posting on twitter

3.For sending regular SMS having bitcoin price.

### Emergency bitcoin price notification applet

#### For E-Mail.

1.Choose a 'webhook' service and slect the 'Recieve a web request' trigger.

2.Name the event 'bitcoin_emergency_email'.

3.For action select 'Email' and choose Send me an email'.

4.Provide the Suject like 'Bitcoin Emergency Price Notification'. Also give the Body like 'Hello, Bitcoin Price goes below your expectation at price : {{Value1}}'. '

#### For Posting Tweets on Twitter.

1.Choose a 'webhook' service and slect the 'Recieve a web request' trigger.

2.Name the event 'bitcoin_emergency_twitter'.

3.For action select 'Twitter' and choose 'Post a Tweet'. Now connect it via your Twitter account. Once it is connected Create the Action.

4.Provide the Message and 'Finish' it.

#### For Regular Bitcoin Upadates.

1.Choose a 'webhook' service and slect the 'Recieve a web request' trigger.

2.Name the event 'regular_bitcoin_updates'.

3.For action select 'Android SMS' and choose 'Send an SMS'.

4.Provide the phone number and type a message 'Hello, Here is currently Bitcoin price at : {{Value1}}'. and create the Applet.


#### For making a google sheet to record all the bitcoin related notifiction recieved by SMS.

1.Select 'Android SMS' as a service.

2.Pass the Keyword ('Bitcoin') by which you want to fetch the SMS and Save it to Google Sheets and create trigger.

3.Choose 'Google sheets' service and 'Add row to spreadsheet' as action.

4.Provie details like Spreadsheet Name 'SMS by match search'. Formatted row and drive folder path.You can leave them as by default has some default vaules.

5.Create an action.


##### Now time to write code and connect all of them with  program code.

Make a boiler plate like below

```python
import requests
import time
from datetime import datetime

def main():
    pass

if __name__ == '__main__':
    main()
```

Next, we have to make an appropriate fucntions to use Applets that we have make ablve.

Add the below code above the main fucntion.

```python
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/hhXkyPpLFoBWtHNmG0x8tEgXdf1PJSRWiQf40jG3Hk-'


   # Extract the price from API response.
   # See code for better understanding
   # Example
   
def latest_bitcoin_price():
  response = session.get(BITCOIN_API_URL, params=parameters)
    data = json.loads(response.text)
    data_float = float(data['data'][0]['quote']['USD']['price'])
    return data_float
    
# Post function for posting request to IFTTT
# Example

def post_ifttt_webhook(event, value):
    data = {'value1': value}
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)
    requests.post(ifttt_event_url, json=data)
```

###### Now Define main() fucntion to arrange all the above function and some conditions based on which our Applet works.

First we need to use of Command line Parsing as we are using some command line customization for better flexibility.

```python
import argparse
```

This argparser helps as to manage different command line arguments.

###### Examples

```python
parser = argparse.ArgumentParser(description='Bitcoin Notifier')
parser.add_argument('-i', '--interval', type=float, nargs=1,
                        metavar='interval', default=[0.3], help='Time Interval in Minuits.')

parser.add_argument('-t', '--threshold', type=int, nargs=1,
                        metavar='threshold', default=[10000], help='Threshold in USD')
```

Basic syntax for ArgumentPaser and .add_argument is

```
ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True)

ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
```
You can Learn [Command Line Parsing](https://docs.python.org/3/library/argparse.html)

###### Now it's time to define some conditions

As we want to get Emergency Notification when the Price of Bitcoin falls below some THRESHOLD_PRICE, we need to define some conditions.

```python
   # For Example
   
 if price < BITCOIN_PRICE_THRESHOLD:
 
 # POST a IFTTT webhoook 'Email'
         post_ifttt_webhook('bitcoin_price_emergency', price)
```

Also for regular notification lets make a bundle of 5- 10 notification and send it as SMS.

```python
bitcoin_storage
if len(bitcoin_storage) == 5:
            post_ifttt_webhook('bitcoin_price_update', 
                               format_bitcoin_history(bitcoin_history))
```

Define some time interval 

```python
 # sleeps for 60 min
 time.sleep(60 * 60)
```

For formatting the body of SMS  define a function like example

```python
def formate_body:
    date=bitcoin_storage['date'].strftime(%d.%m.%Y %H:%M)
    price=bitcoin_storage['price']
    row = 'date - {}: , price- ${}'.format(date,price)
    row.append(row)
```

## Running a Program

To rum your price notification program, execute the folling in your command-line terminal.

```shell
$ python bitcoin_notification_app.py
```

## Results

#### Email 
![alt text](https://github.com/avinash-mahawar-au5/Bitcoin-Notification-Program_python/blob/master/Images/Email.png?raw=true)
