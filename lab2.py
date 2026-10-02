'''
Author(s):   Samantha Vialpando, Noah Webb
Assignment:  Lab 2
Date:        Sept. 29, 2026
Description: This program is a credit calculator
             that takes the user's name, total credits,
             and prints a receipt for that term and the
             total cost of the credits.
Input:       string name, term
             int credits
Output:      int credit_price
References:  Lab 2 specifications, week 2 modules
'''
from datetime import datetime

# Samantha
def welcome_message():
    '''
    This function prints a welcome message to the user.
    params: none
    returns: none
    '''
    print("This is the term credit calculator. to get started,\n"
          "Follow the prompts below.\n")

# Samantha
def display_menu():
    '''
    This function displays a menu of term options to the user.
    params: none
    returns: (int) term
    '''
    print("Select term from the following options:\n")
    print("1. Fall")
    print("2. Winter")
    print("3. Spring")
    print("4. Summer")
    temp_val = int(input("Select 1, 2, 3, or 4: "))
    while temp_val > 4 or temp_val < 1:
        print("Invalid input!")
        temp_val = int(input("Must enter 1, 2, 3, 4: "))

    if temp_val == 1:
        term = "Fall"
    elif temp_val == 2:
        term = "Winter"
    elif temp_val == 3:
        term = "Spring"
    else:
        term = "Summer"
    return term

# Samantha
def get_credits(credits, classes_counter):
    '''
    this function asks the user to input a number of credits
    per term. It allows the user to input mulitple times to
    simulate mulitple classes, with a credit cap of 18.
    params: none
    returns: (int) credits
    '''
    more_credits = "yes"

    while more_credits == "yes" or more_credits == "y":
        classes_counter += 1
        temp_var = int(input("Enter the number of credits for a class: "))
        # added this as a check for negative or too large credit values
        while temp_var < 1 or temp_var > 18:
            print("Invalid input. Please enter a credit value between 1 and 18.")
            temp_var = int(input("Enter the number of credits for a class: "))
        if credits + temp_var >= 18:
            print("You have reached the maximum number of credits (18). You cannot add more.")
            # made this so it keeps your credit value instead of making it 18 automatically
            # that way if they dont want to add that last score they dont have to
            credits = credits
        else:
            credits += temp_var

        more_credits = input("Would you like to input more credits? (y/n): ")
        while more_credits.lower() not in ["yes", "y", "no", "n"]:
            print("Invalid input. Please enter 'yes' or 'no'.")
            more_credits = input("Would you like to input more credits? (y/n): ")



    return credits, classes_counter

# Noah
def total_price(credits, price):
    total_price = (credits * price)
    return total_price

# Noah
def print_receipt(name, term, classes_counter, credits, total):
    '''
    This function prints a receipt for the user.
    params: (string) name, (string) term, (int) classes_counter, (int) credits, (float) total
    returns: none
    '''
    
    current_datetime = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    print("\nThank you for using the credit calculator!")
    print("\n-------- Receipt --------")
    print("Date:", current_datetime)
    print("{: <17}{: <3}".format("Name: ", name.capitalize()))
    print("{: <17}{: <3}".format("Term: ", term))
    print("{: <17}{: <3}".format(("Classes: "), classes_counter))
    print("{: <17}{: <3}".format("Total credits: ", credits))
    print(f"Your total is: ${round(total,2):.2f}")
    print("-------------------------")

# Noah
def main():
    credits, classes_counter = 0, 0
    price = 244.795 # 3 digits so round() is used or simulate tax
    total = 0.0

    welcome_message()

    name = str(input("Enter your name: "))
    term = display_menu()
    credits, classes_counter = get_credits(credits, classes_counter)
    total = total_price(credits, price)

    print_receipt(name, term, classes_counter, credits, total)

if __name__ == "__main__":
    main()
