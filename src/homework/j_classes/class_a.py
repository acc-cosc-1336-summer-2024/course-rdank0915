#Write a class that models a die and returns it’s rolled value

#Import the random function to control the value of the die when rolled
import random

#The Die class simulates rolling of a die
class Die:

    #Initialize the roll_value data attribute with an initial value of None
    def __init__(self):
        self.__roll_value = None
    
    #The roll method generates a random number between 1 and 6
    def roll(self):
        self.__roll_value = random.randint(1, 6)
    
    #The get_rolled_value method returns the rolled value
    def get_rolled_value(self):
        return self.__roll_value
    
    #The __str__ method formats the output as a string
    def __str__(self):
        return f"The rolled value is: {self.__roll_value}"
    
def display_menu():
    print("Homework 7 Menu")
    print("1-Roll the Die")
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
    
def option_1(self):
    print = ("Rolling the Die... ")
    print(self.__str__)

def option_2():
    choice = input("Would you like to exit Y or N: ")
    if choice == "Y":
        print("Exiting... ")
    elif choice == "N":
        run_menu()
    else:
        print("Invalid Option")

        