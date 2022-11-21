import requests

class RealTimeCurrencyConverter():
    def __init__(self,url):
        self.data= requests.get(url).json()
        self.currencies = self.data['rates']

def convert(self, from_currency, to_currency, amount):
    initial_amount = amount
    #first convert it into USD if it is not in USD.
    # because our base currency is USD
    if from_currency != 'USD' :
        amount = amount / self.currencies[from_currency]

        # limiting the precision to 4 decimal places
    amount = round(amount * self.currencies[to_currency], 4)
    return amount

url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = RealTimeCurrencyConverter(url)
print(converter.convert('INR','USD',100))
