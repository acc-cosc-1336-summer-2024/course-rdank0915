import decisions

options = float(input("Enter the number for options: ")) #Write code to prompt the user for the value for options
total = float(input("Enter the number for total: ")) #Write code to prompt the user for the value for total

ratio = decisions.get_options_ratio(options, total)
rating = decisions.get_faculty_rating(ratio)

print(rating)