L = list(map(str, input("Enter the course you are taking, followed by the grade you currently have in that course.\n").split(',')))

if len(L) < 2:
    print("This is an invalid input.")
elif len(L) >= 2:
    print(L)

#could delete, remove, or pop the indexes that are the course names, and then turn the remaining indexes of the list str to int, then calculate it that way
#could sort the list, and then remove every entry that is longer than two characters, however could pose challenges in case the user inputs floats
    


i = 0
grades = []
for data in L:
    grades.append(L[i])
    i = i+2
print(grades,i)
