#Write code to compare 2 strings character by character and return a value representing the difference
#between the two

def get_p_distance(list1, list2):

    distance = 0

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            distance += 1
    return distance

#Write code to compare 2 strings character by character and return a value representing the difference
#between the two



def display_menu():
    print("Homework 6 Menu")
    print("1-P Distance Matrix")
    print("2-Exit")

def run_menu():
    option = "1"
    while(option != "2"):
        display_menu()
        option = input("Enter your menu option: ")
        handle_menu_option(option)

def handle_menu_option(option):
    if(option == '1'):
        option_1()
    elif(option == '2'):
        option_2()
    else:
        print("Invalid Option")

def option_1():
    list1 = input("Enter your first list: ")
    list2 = input("Enter your second list: ")
    print(get_p_distance(list1, list2))

def option_2():
    choice = input("Would you like to exit Y or N: ")
    if choice == "Y":
        print("Exiting... ")
    elif choice == "N":
        run_menu()
    else:
        print("Invalid Option")