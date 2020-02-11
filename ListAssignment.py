# Sam Cole
# 2/10/2020


def sumlist(numbers):
    for number in numbers:
        total = 0
        total = number + total
    return f"The sum of the list is {total}"


def productlist(numbers):
    for number in numbers:
        product = 1
        product = number * product
    return f"The product of the list is {product}"


def meanlist(numbers):
    total =
    mean = total / 5
    return f"the mean is {mean}"


def medainlist(numbers):
    return f"The median of the list is {numbers[2]}"


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
