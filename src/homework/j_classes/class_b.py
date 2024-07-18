from src.homework.j_classes.class_a import Die

def display_menu():
    print("Homework 7 Menu")
    print("1-Roll the Die")
    print("2-Exit")

def run_menu():
    die_val = Die()
    option = "1"
    while(option != "2"):
        display_menu()
        option = input("Enter your menu option: ")
        handle_menu_option(option, die_val)

def handle_menu_option(option):
    if(option == '1'):
        option_1()
    elif(option == '2'):
        option_2()
    else:
        print("Invalid Option")

def option_1(die_val):
    die_val.roll()

    choice = "Y"
    while(choice == "Y" or choice == "N"):
        choice = input("Would you like to exit Y or N: ")
        if choice == "Y":
            print(run_menu())
        elif choice == "N":
            print(option_1())

def option_2():
    choice = input("Would you like to exit Y or N: ")
    if choice == "Y":
        print("Exiting... ")
    elif choice == "N":
        run_menu()
    else:
        print("Invalid Option")