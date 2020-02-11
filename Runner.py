# Sam Cole
# This is the runner
import ListAssignment
numbers = [5, 6, 7, 5, 9]

numbers.sort()
print(numbers)
print(f"ListAssignment.sumlist(numbers))
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
