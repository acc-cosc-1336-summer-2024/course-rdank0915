#This program will create a menu-driven program, 
#calculate a factorial function, and perform a simple addition function

def get_factorial(num):

    result = 1

    for val in range(1, num + 1):

        result *= val

    return result

def sum_odd_numbers(num):

    sum = 0
    val = 1

    while val <= num:
        if val % 2 != 0:
            sum += val

    return sum

