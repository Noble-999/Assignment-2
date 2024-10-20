# Task 1 ==> Leap Year Checker

year = int(input("Please enter the year you are in: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("True, that is a leap year!")
else:
    print("Flase, that is not a leap year!")

# the '!=' and 'or' conditions helped me out very much.
# My original thought was an if not statement but everything returned "true".