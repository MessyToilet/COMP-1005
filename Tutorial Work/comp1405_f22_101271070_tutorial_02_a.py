'''
Date:           9/29/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Birthday Calculator
'''

userName    = str(input("What's your name? "))          #Ask user for name
currentYear = int(input("What year is it? "))           #ask user for year
birthYear   = int(input("What year were you born? "))   #ask user for birth year

birthYearCalculated     = currentYear - birthYear       #calculate age
birthYearCalculated2    = birthYearCalculated - 1       #calculate age if birthday hasn't passed
leapBrithday = int(birthYearCalculated/ 4)              #calculate leap year age 
"""
if str(input("Are you born on a leap year? n/y ")) in ["y", "Y"]:
    leapBrithday = int(birthYearCalculated/ 4)
    print(leapBrithday)
    
else:
    print("Your name is " + str(userName) + " and you are " + str(birthYearCalculated) + " or " + str(birthYearCalculated2) + " years old.")
"""

print("You could be " + str(birthYearCalculated) + " or " + str(birthYearCalculated2) + " and if you were born on a leap year " + str(leapBrithday))  #print results