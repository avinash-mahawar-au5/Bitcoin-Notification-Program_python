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

2.Name the event 'bitcoin_emergency_email'.

3.For action select 'Twitter' and choose 'Post a Tweet'. Now connect it via your Twitter account. Once it is connected Create the Action.

4.Provide the Message and 'Finish' it.

### For Regular Bitcoin Upadates.

1.Choose a 'webhook' service and slect the 'Recieve a web request' trigger.

2.Name the event 'regular_bitcoin_updates'.

3.For action select 'Android SMS' and choose 'Send an SMS'.

4.Provide the phone number and type a message 'Hello, Here is currently Bitcoin price at : {{Value1}}'. and create the Applet.



