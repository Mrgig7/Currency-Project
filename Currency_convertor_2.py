from currency_converter import CurrencyConverter

def main():
    print("This is a currency converter project.")
    print("You can use these currency ('INR','USD','EUR', 'JPY') ")

    amount = float(input("Enter the amount you want to convert : "))

    curr_currency = input("Enter the currency which you currently have : ".casefold())
    want_currency = input("Enter the currency you want to have : ".casefold())

    # CurrencyConverter.convert()
    c = CurrencyConverter()

    converted_amount = c.convert(amount,curr_currency,want_currency)

    print(f"{amount} {curr_currency} is {converted_amount} {want_currency} ")


main()