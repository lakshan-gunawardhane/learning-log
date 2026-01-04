import sys

def main():
    #check for, are there inputs
    if len(sys.argv) == 2:
        cli_input = sys.argv[1] 
        #clean inputs if it is available
        cleaned_input = cli_input.strip().lower()
    
    #if its not valid, tell the user to try again in cli
    else:
        print("try again")

if __name__ == "__main__":
    main()
