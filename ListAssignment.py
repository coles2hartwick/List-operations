# Sam Cole
# 2/10/2020

# finds the sum of the list
def sumlist(numbers):
    total = 0
    for number in numbers:
        total = number + total
    return total

# finds the product of the list
def productlist(numbers):
    product = 1
    for number in numbers:
        product = number * product
    return product

# finds the mean of the list
def meanlist(numbers):
    total = sumlist(numbers)
    mean = total / 5
    return mean

# finds the median of the list
def medainlist(numbers):
    return numbers[2]

# finds the mode of the list
def modelist(numbers):
    if numbers[0] == numbers[1] or numbers[2] or numbers[3] or numbers[4]:
        mode = numbers[0]
    elif numbers[1] == numbers[2] or numbers[3] or numbers[4]:
        mode = numbers[1]
    elif numbers[2] == numbers[3] or numbers[4]:
        mode = numbers[2]
    elif numbers[3] == numbers[4]:
        mode = numbers[3]
    else:
        return "There is no mode sorry"
    return f"The mode is {mode}"

# finds the largest number in the list
def largestnum(numbers):
    return numbers[4]

# finds the smallest number in the list
def smallestnum(numbers):
    return numbers[0]

# deletes the duplicates in a list
def noduplicates(numbers):
    if numbers[0] == numbers[1]:
        del numbers[0]
    elif numbers[0] == numbers[2]:
        del numbers[0]
    elif numbers[0] == numbers[3]:
        del numbers[0]
    elif numbers[0] == numbers[4]:
        del numbers[0]
    elif numbers[1] == numbers[2]:
        del numbers[1]
    elif numbers[1] == numbers[3]:
        del numbers[1]
    elif numbers[1] == numbers[4]:
        del numbers[1]
    elif numbers[2] == numbers[3]:
        del numbers[2]
    elif numbers[2] == numbers[4]:
        del numbers[2]
    elif numbers[3] == numbers[4]:
        del numbers[3]
    else:
        return "There is no duplicates"
    return numbers

# deletes the even numbers in a list
def noeven(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            del numbers[count]
        count = count + 1
    return numbers

# deletes the odd numbers in a list
def noodd(numbers):
    count = 0
    for number in numbers:
        if number % 2 != 0:
            numbers.remove(number)
            #del numbers[count]
        count = count + 1
    return numbers

# checks to see if a number is in the list
def isitthere(numbers, guess):
    for number in numbers:
        if guess == number:
            return "Its in there alright"
        else:
            return "Sorry not in there"
