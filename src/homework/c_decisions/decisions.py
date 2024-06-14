def get_options_ratio(options, total): #This defines the parameters which will be used in the equation to find the ratio
    ratio = options / total #This is the equation to calculate the ratio
    return(ratio) #This tells Python to give the result of the above equation

def get_faculty_rating(ratio): #This tells Python to extract the result from the equation that was used to calculate the ratio
    if(ratio <= 1 and ratio >= .9): #and evaluate it based on the ranges in lines 6-15
        return 'Excellent'
    if(ratio < .9 and ratio >= .8):
        return 'Very Good'
    if(ratio < .8 and ratio >= .7):
        return 'Good'
    if(ratio < .7 and ratio >= .6):
        return 'Needs Improvement'
    if(ratio < .6 and ratio >= .0):
        return 'Unacceptable'
