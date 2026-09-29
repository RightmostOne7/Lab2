'''
Author(s):   Samantha Vialpando, Noah Webb
Assignment:  Lab 2
Date:        Sept. 29, 2026
Description: This program will be a log, of
             each time a student submits their grades. 
             It will display the date and time of the 
             submission, and all of the known grades.
Input:
Output: 
References:
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
