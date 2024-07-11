#Write code to compare 2 strings character by character and return a value representing the difference
#between the two

def get_p_distance(list1, list2):

    distance = 0

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            distance += 1

    p_distance = distance / len(list1)

    return p_distance

#Write code that computes the distance matrix for a given list of four elements by using the get_p_distance function
#to compute their distances, and then iterate through all pairs of elements

def get_p_distance_matrix(list1):

    rows = len(list1)
    cols = len(list1)

    D_matrix = []

    for i in range(0, rows):
        row_list = []
        for j in range(0, cols):
            list_a = list1[i]
            list_b = list1[j]
            matrix_index = (get_p_distance(list_a, list_b))
            row_list.append(matrix_index)
        D_matrix.append(row_list)

    return D_matrix
    

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

    matrix = []

    list1 = input("Enter first taxa: ")
    matrix.append(list1)
    list2 = input("Enter second taxa: ")
    matrix.append(list2)
    list3 = input("Enter third taxa: ")
    matrix.append(list3)
    list4 = input("Enter fourth taxa: ")
    matrix.append(list4)

    print(get_p_distance_matrix(matrix))

def option_2():
    choice = input("Would you like to exit Y or N: ")
    if choice == "Y":
        print("Exiting... ")
    elif choice == "N":
        run_menu()
    else:
        print("Invalid Option")