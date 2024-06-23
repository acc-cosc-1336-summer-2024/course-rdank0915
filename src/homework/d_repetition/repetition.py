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
        
        sum = sum + val

        val += 2

    return sum

def display_menu():
    print("Homework 3 Menu")
    print("1-Factorial")
    print("2-Sum Odd Numbers")
    print("3-Exit")

def run_menu():
    option = "1"
    while(option != "3"):
        display_menu()
        option = input("Enter your menu option: ")
        handle_menu_option(option)

def handle_menu_option(option):
    if(option == '1'):
        option_1()
    elif(option == '2'):
        option_2()
    elif(option == '3'):
        option_3()
    else:
        print("Invalid Option")

def option_1():
    num = int(input("Enter a number between 0 and 10: "))
    if num > 0 and num < 10:
        print(get_factorial(num))
    else:
        num = int(input("Number invalid..Please enter a number between 0 and 10: "))
        if num > 0 and num < 10:
            print(get_factorial(num))

    choice = "Y"
    while(choice == "Y" or choice == "N"):
        choice = input("Would you like to exit Y or N: ")
        if choice == "Y":
            print(run_menu())
        elif choice == "N":
            print(option_1())

def option_2():
    num = int(input("Enter a number between 0 and 100: "))
    if num > 0 and num < 100:
        print(sum_odd_numbers(num))
    else:
        num = int(input("Number invalid..Please enter a number between 0 and 100: "))
        if num > 0 and num < 100:
            print(sum_odd_numbers(num))
    
    choice = "Y"
    while(choice == "Y" or choice == "N"):
        choice = input("Would you like to exit Y or N: ")
        if choice == "Y":
            print(run_menu())
        elif choice == "N":
            print(option_2())

def option_3():
    choice = input("Would you like to exit Y or N: ")
    if choice == "Y":
        print("Exiting... ")
    elif choice == "N":
        run_menu()
    else:
        print("Invalid Option")
    
    
    