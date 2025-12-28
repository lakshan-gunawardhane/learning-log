import sys
import requests

#taking the crypto price in usd
def get_price(coin_name):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_name.lower()}&vs_currencies=usd"
        response = requests.get(url, timeout=5)
        data = response.json()
        
        price = data[coin_name.lower()]['usd']
        return price
    except:
        return 0
    
def main():
    if len(sys.argv) < 3 or len(sys.argv) % 2 == 0:
        print("Usage: python day07_portfolio.py <coin> <amount> <coin> <amount>...")
        sys.exit()
    
    print(f"{'COIN':<15} {'AMOUNT':<10} {'PRICE':<15} {'VALUE ($)':<15}")
    print("-" * 60)

    total_net_worth = 0

    for i in range(1, len(sys.argv), 2):
        coin_name = sys.argv[i]

        try:
            coin_amount = float(sys.argv[i + 1])
        except ValueError:
            print(f"❌ Error: {sys.argv[i+1]} is not a number.")
            continue

        price = get_price(coin_name)

        if price == 0:
            print(f"❌ Could not find price for {coin_name}")
            continue
        
        value = price * coin_amount
        total_net_worth += value

        print(f"{coin_name.upper():<15} {coin_amount:<10.2f} ${price:<14,.2f} ${value:,.2f}")

    print("-" * 60)
    print(f"💰 TOTAL NET WORTH: ${total_net_worth:,.2f}")

if __name__ == "__main__":
    main()
    
