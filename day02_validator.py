#defining the main function
def main():
    #starting a loop until setting a huge target income
    while True:
        target_monthly_income = value_error_solver("What is your target monthly income?: $")
        if target_monthly_income < 1000:
            print("Thinking too small. Try again")
        else:
            print(f"Target set: ${target_monthly_income}")
            break

#defining a function to get valid values to my project
def value_error_solver(value):
    while True:
        try:
            number_value = int(input(value))
            #ask below conditional , because of incomes cant be minus
            if number_value < 0:
                print("minus???")
            else:
                return number_value
        except ValueError:
            print("Invalid input. Enter a clean number.")

#calling the main function
main()
