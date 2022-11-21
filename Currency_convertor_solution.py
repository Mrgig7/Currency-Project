import requests

from_currency = str (
    input("Enter in the currency you'd like to exchange from: ")).upper()

to_currency = str (
    input("Enter in the currency you'd like to comvert to: ")).upper()

amount = float(input("Enter in the amount you'd like to exchange: "))

response = requests.get(
    f'https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}')

print(
    f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}" )
