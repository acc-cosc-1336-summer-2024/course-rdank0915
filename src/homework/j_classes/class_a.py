#Write a class that models a die and returns it’s rolled value

#Import the random function to control the value of the die when rolled
import random

class Die:

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
    


        