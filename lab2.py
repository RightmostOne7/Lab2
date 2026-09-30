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
# Noah
def main():
    price = 100

    
    name = str(input("Enter your name: "))
    print(name.capitalize())
    credits = int(input("Enter your total number of credits: "))
    print(credits)
    print("Your credit total is: $", credit_price(credits, price))

if __name__ == "__main__":
    main()
