import sys

def main():
    # Check if the user provided a name
    if len(sys.argv) < 2:
        print("Hello, stranger!")
    else:
        # Capture the name from the command line
        name = sys.argv[1]
        print(f"Hello, Architect {name}")

# The Gatekeeper
if __name__ == "__main__":
    main()