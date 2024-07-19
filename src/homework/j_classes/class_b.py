import class_a

def display_menu():
    print("Homework 7 Menu")
    print("1-Roll the Die")
    print("2-Exit")

def run_menu():
    option = "1"
    while(option != "2"):
        display_menu()
        option = input("Enter your menu option: ")
        if option == '2':
            print("Exiting the program...")
            break
        handle_menu_option(option)

def handle_menu_option(option):
    if(option == '1'):
        option_1()
    else:
        print("Invalid Option")

def option_1():
    
    die = class_a.Die()

    die.roll()
    die_val = str(die)
    print(die_val)

    choice = "Y"
    while(choice == "Y" or choice == "N"):
        choice = input("Would you to roll again Y or N: ")
        if choice == "Y":
            print(option_1())
        elif choice == "N":
            print(run_menu())