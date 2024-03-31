import os
L = list(map(str, input("\nEnter the course you are taking, followed by the grade you currently have in that course: ").split(',')))
Grades = L[1::2]
Amount = len(Grades)
if len(L) < 2:
    print("\nThis is an invalid input.\n")
elif len(L) >= 2:
    GradesToInt = [eval(i) for i in Grades]
    Total = 0
    for num in GradesToInt:
        Total += num
    CGPA = Total / Amount

    print("\nYour cumulative grade point average (CGPA) is \033[1m" + str(CGPA) + "\033[0m%\n") #to concatenate and remove the space between the percent and the CGPA, you have to turn it into a string since you cannot concactenate a float
    

#could delete, remove, or pop the indexes that are the course names, and then turn the remaining indexes of the list str to int, then calculate it that way
#could sort the list, and then remove every entry that is longer than two characters, however could pose challenges in case the user inputs floats
