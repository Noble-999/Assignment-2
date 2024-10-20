# Task 1 ==> Identify the Greastest
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
third_number = float(input("Enter the third number: "))

if first_number >= second_number and first_number >= third_number:
    largest = first_number
elif second_number >= first_number and second_number >= third_number:
    largest = second_number
else:
    largest = third_number

print("The Largest number is:", largest)


# question: Is there a way you could clean up this code with the max statement?



# Task 2 ==> Identify the Smallest
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
third_number = float(input("Enter the third number: "))

if first_number <= second_number and first_number <= third_number:
    smallest = first_number
elif second_number <= first_number and second_number <= third_number:
    smallest = second_number
else:
    smallest = third_number


print("The smallest number is:", smallest)