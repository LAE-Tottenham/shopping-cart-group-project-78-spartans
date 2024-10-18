import requests #This is for API interfacing
import math

url = 'https://v6.exchangerate-api.com/v6/9539da403e1974365970d782/latest/GBP'

response = requests.get(url)
data = response.json()

# exchange_rates = {
#     'USD': 1.13,
#     'EUR': 1.15,
#     'YEN': 1195.23,
#     'AUD': 1.94,
#     'CAD': 1.8,
#     'CHF': 1.13,
#     'HKD': 10.15,
#     'NZD':2.15,
#     'SGD':1.71,
# }
# symbols = {
#     'USD':"US$",
#     'EUR':"€",
#     'YEN':'¥',
#     'AUD':'AU$',
#     'CAD':'CA$',
#     'CHF':'₣',
#     'HKD':'HK$',
#     'NZD':'NZ$',
#     'SGD':'S$',  
#}

def check_currency_exists(initc,finc): # currency before and after exchange
    TF = False if finc not in data["conversion_rates"] or initc != 'GBP' else True
    return TF

def validate_amount(amount):
    TF = False if float(amount) > 1000 or float(amount) < 10 else True
    return TF
    
def currency_convert(newc, amount): # Converts and rounds to new currency
    conver = data["conversion_rates"][newc]
    nam = float(amount) * float(conver) 
    nam = round(nam) if newc.upper() == "YEN" else round(nam,2)
    return nam

def convertornot(amount, currency):
    x = input("Would you like to convert the price to another currency? (y/n)").lower()
    if x.lower() == "y":
        print('\n'.join(data["conversion_rates"].keys()))
        newc = input("What currency would you like to convert into? ").upper()
        if check_currency_exists(currency,newc) and validate_amount(amount):
            converted = currency_convert(newc,amount)
            return "Great, you now must pay "+ str(newc) + " " + str(converted)
        else:
            return "Invalid Conversion, you must pay £" + str(amount)
    else:
        return "Okay, you must pay £ "+ str((amount))
