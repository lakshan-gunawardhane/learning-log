import requests
import json

def get_rates():
    try:
        url = "https://open.er-api.com/v6/latest/USD"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['rates']
    except requests.RequestException:
        print("Error: Could not connect to currency server.")
        return None
    
def main():
    # 1. Fetch data safely
    rates = get_rates()
    if not rates:
        import sys
        sys.exit()

    input_amount = taking_input_amounts()

    while True:
        try:
            input_currency =input("IN currency type: ").upper()
            input_currency_rate = (rates[input_currency])
            break
        except:
            print("enter valid inputs")

    while True:
        try:    
            output_currency = input("OUT currency type: ").upper()
            output_currency_rate = (rates[output_currency])
            break
        except:
            print("enter valid inputs")

    output_amount = (input_amount / input_currency_rate) * output_currency_rate

    print(f"{input_amount}{input_currency} = {output_amount}{output_currency}")

def taking_input_amounts():
    while True:
        try:
            input_amount = float(input("Tell me the amount: "))
            return input_amount
        except ValueError:
            print("enter valid inputs")

main()            