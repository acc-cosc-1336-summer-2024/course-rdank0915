#Write code to compare 2 strings character by character and return a value representing the difference
#between the two

def get_hamming_distance(dna1, dna2):

    distance = 0

    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            distance += 1
    return distance

#Write code to get a DNA sequence from a user, reverse the sequence, and then replace A's with T's and C's with G's return a value representing the complement
#between the two

def get_dna_complement(dna):

    dna_reverse = dna[::-1]
    
    complement = ""
    for i in dna_reverse:
        if i == 'A':
            complement += 'T'
        elif i == 'T':
            complement += 'A'
        elif i == 'C':
            complement += 'G'
        elif i == 'G':
            complement += 'C'
    
    return complement

def display_menu():
    print("Homework 5 Menu")
    print("1-Hamming Distance")
    print("2-DNA Complement")
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
    dna1 = input("Enter DNA Sequence 1: ")
    dna2 = input("Enter DNA Sequence 2: ")
    print(get_hamming_distance(dna1, dna2))

def option_2():
    dna = input("Enter DNA Sequence: ")
    print(get_dna_complement(dna))

def option_3():
    choice = input("Would you like to exit Y or N: ")
    if choice == "Y":
        print("Exiting... ")
    elif choice == "N":
        run_menu()
    else:
        print("Invalid Option")
