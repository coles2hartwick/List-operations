# Sam Cole
# This is the runner
import ListAssignment

first = int(input("Please enter a whole number"))
second = int(input("Please enter a whole number"))
third = int(input("Please enter a whole number"))
fourth = int(input("Please enter a whole number"))
fifth = int(input("Please enter a whole number"))
numbers = [first, second, third, fourth, fifth]

numbers.sort()
print(f"The sum of the list is {ListAssignment.sumlist(numbers)}")
print(f"The product of the list is {ListAssignment.productlist(numbers)}")
print(f"The mean is {ListAssignment.meanlist(numbers)}")
print(f"The median is {ListAssignment.medainlist(numbers)}")
print(ListAssignment.modelist(numbers))
numbers2 = list(numbers)
print("There are no more duplicates")
print(ListAssignment.noduplicates(numbers2))
numbers2 = list(numbers)
print("I deleted all the even numbers")
print(ListAssignment.noeven(numbers2))
numbers2 = list(numbers)
print("I deleted all the odd numbers")
print(ListAssignment.noodd(numbers2))
guess = input("Type a number to see if its in the list")
print(ListAssignment.isitthere(numbers, guess))
