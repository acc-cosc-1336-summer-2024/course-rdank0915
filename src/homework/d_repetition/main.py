import repetition

def display_menu():
    print("Homework 3 Menu")
    print("1-Factorial")
    print("2-Sum Odd Numbers")
    print("1-Exit")

def run_menu():

    option = "1"

    while(option != "3"):
        display_menu()
        option = input("Enter your menu option: ")
        handle_menu_option(option)

def handle_menu_option(option):

    if(option == 1):
        option_1()
    elif(option == 2):
        option_2()
    elif(option == 3):
        print("Exiting...")
    else:
        print("Invalid Option")

def option_1():
    num = float(input("Enter a number: "))
    result = repetition.get_factorial(num)
    print(result)

def option_2():
    num = float(input("Enter a number: "))
    result = repetition.sum_odd_numbers(num)
    print(result)
