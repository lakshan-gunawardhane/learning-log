import sys
from colorama import init, Fore, Style

# 1. Initialize the color engine (Required for Windows)
init()

def main():
    # 2. Check input
    if len(sys.argv) < 2:
        # RED text for "Error/Warning"
        print(Fore.RED + "⚠️  Error: You forgot to tell me your name." + Style.RESET_ALL)
        print("Usage: python day04_greeter.py [Name]")
    else:
        name = sys.argv[1]
        # GREEN text for "Success"
        print(Fore.GREEN + f"✅ Access Granted. Welcome, Architect {name}." + Style.RESET_ALL)

if __name__ == "__main__":
    main()