from currency_converter import CurrencyConverter

def convert_currency (amount, from_currenty, to_currency):

    c = CurrencyConverter()

    result = c.convert(amount, from_currenty, to_currency)

    return resul

amount = float(input("Enter the amount to convert: "))

from_currency = input("Enter the currency to convert from: ").upper()

to_currency = input("Enter current to convert to: ").upper()

converted_amount = convert_currency(amount, from_currency, to_currency)

print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")