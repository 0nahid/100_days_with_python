number1 = 10
number2 = 20
number3 = 30

# calculate the sum of the numbers with the help of the function


def sum_of_numbers(number1, number2, number3):
    sum = number1 + number2 + number3
    return sum


# call the function
sum = sum_of_numbers(number1, number2, number3)
print("The sum of the numbers is: ", sum)

# calculate the average of the numbers with the help of the function


def average_of_numbers(number1, number2, number3):
    average = (number1 + number2 + number3) / 3
    return average


# call the function
average = average_of_numbers(number1, number2, number3)
print("The average of the numbers is: ", average)
