'''
Author(s):   Samantha Vialpando, Noah Webb
Assignment:  Lab 2
Date:        Sept. 29, 2026
Description: This program is a credit calculator
             that takes the user's name, total credits,
             and prints a reciept for that term and the
             total cost of the credits.
Input:       string name, term
             int credits
Output:      int credit_price
References:  Lab 2 specifications, week 2 modules
'''
from datetime import date, time, datetime
# Noah
def credit_price(credits, price):
    credit_price = credits * price
    return credit_price

def get_credits(credits):
    '''
    this function asks the user to input a number of credits
    per term. It allows the user to input mulitple times to
    simulate mulitple classes, with a credit cap of 18.
    params: none
    returns: (int) credits
    '''
    more_credits = "yes"
    while more_credits == "yes" or more_credits == "y":
        temp_var = int(input("Enter the number of credits for a class: "))
        if credits + temp_var >= 18:
            print("You have reached the maximum number of credits (18). You cannot add more.")
            credits = 18
        else:
            credits += temp_var
        
        more_credits = input("Would you like to input more credits? (y/n): ")
        while more_credits.lower() not in ["yes", "y", "no", "n"]:
            print("Invalid input. Please enter 'yes' or 'no'.")
            more_credits = input("Would you like to input more credits? (y/n): ")

    return credits

# samantha
def welcome_message():
    '''
    This function prints a welcome message to the user.
    params: none
    returns: none
    '''
    print("This is the term credit calculator. to get started,\n"
          "Follow the prompts below.\n")

#samantha
def display_menu(term):
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

# Noah
def main():
    credits = 0
    price = 244.78
    welcome_message()
    
    name = str(input("Enter your name: "))
    term = display_menu(term)
    credits = get_credits(credits)


    # this print statement we will eventually replace with a 
    # print reciept function. It should print the student name,
    # date time, term, total credits, and total cost.
    # print("Your credit total is: $", credit_price(credits, price))

if __name__ == "__main__":
    main()
