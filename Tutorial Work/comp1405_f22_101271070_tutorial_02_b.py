'''
Date:           9/30/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Magic Numbers
'''

number = int(input("What's your phone number?: "))      #take number from user

#number = 5202600                                       #test

"""
number = str(input("What's your phone number?: "))      #take user number
print("The first index is", number[0])                  #test
print("The second index is", number[1])                 #test
print("The third index is", number[2])                  #test
print("The first three indexs are", number[:3])         #test

lineNum = int(number[3:])                               #define lineNum

prefix = ((((((int(number[:3]) * 80) + 1 ) * 250) +  (2 * lineNum)) - 250)/ 2)  #Calculate prefix
print(str(prefix))                                                              #print prefix
"""

prefix = number // 10005        #divide by 1005, leave decimals 
lineNum = number % 520000       #do mod 520000

#print(prefix)
#print(lineNum)

prefix2 = ((prefix * 80) + 1) * 250     #calculate
lineNum2 = prefix2 + (2 * lineNum)      #calculate
lineNum3 = (lineNum2 - 250) / 2         #calculate

print(int(lineNum3))                    #print result

