import requests

from_currency = str (
    input("Enter the currency code: ")).upper()

to_currency = str (
    input("Enter the currency code you want to convert to: ")).upper()

amount = float(input("Enter the amount you want to convert: "))

response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

print (f"{amount} {from_currency} is equal to {response.json()['rates'][to_currency]} {to_currency}")