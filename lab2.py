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

# samantha
def welcome_message():
    print("This is the term credit calculator. to get started,\n"
          "Follow the prompts below.\n")

#samantha
def display_menu(term):
    print("Select term from the following options:\n")
    print("1. Fall")
    print("2. Winter")
    print("3. Spring")
    print("4. Summer")
    term = int(input("Select 1, 2, 3, or 4: "))
    return term

# Noah
def main():
    name = ""
    credits, term = 0, 0
    price = 244.78
    welcome_message()
    
    name = str(input("Enter your name: "))
    term = display_menu()

    '''
    here i want to add a while loop to ask the user to input
    a number of credits per class until they enter loop
    ending value, like 0. This is where we can use a compound
    operator like += to add the number of credits to the total
    credits variable.
    '''
    # this print statement we will eventually replace with a 
    # print reciept function. It should print the student name,
    # date time, term, total credits, and total cost.
    print("Your credit total is: $", credit_price(credits, price))

if __name__ == "__main__":
    main()
