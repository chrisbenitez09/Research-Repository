'''Write a Python program that takes 10 numbers as input from user and find their sum and average.'''
'''For Python 3.4+, use statistics.mean for numerical stability with floats.'''
import statistics
list = []
number = int(input("How many numbers you want to sum: "))

for x in range(number):
    number = int(input("Enter number: "))
    list.append(number)

print("Sum of the integers given is: ", sum(list))
print("Average of the integers is: ", statistics.mean(list))