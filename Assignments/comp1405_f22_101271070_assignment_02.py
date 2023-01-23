'''
Date:           9/23/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Type conversions and arithmetic operations, from the comand line and user input
'''


import sys      #import sys


if len(sys.argv) > 1:       #if there is a arg given
    try:                    #try...
        int(sys.argv[1])    #check if the arg given is an integer
    except:                 #if it isn't
        print("\n" + "Input given is not an integer, quiting program...")       #print error
        quit()                                                                  #quit program

    inputnum = input("\n" + "Pick your number: ")                               #define var as user input

    try:                                                                        #try...
        int(inputnum)                                                           #check if value given is a integer
    except:                                                                     #if it isn't
        print("\n" + "Input given is not an integer, quiting program...")       #print error
        quit()                                                                  #quit

    print("\n" + "Your number is " + str(sys.argv[1]) + "\n")                   #print the sys arg    
    print("the number you picked is " + str(inputnum))                          #print input 

else:                                                                           #if no arg given
    print("\n" + "Command line arg not given, quiting program...")              #print error
    quit()                                                                      #quit


def calcu():                                                                                        #def calcu
    mod5 = int(sys.argv[1]) % 5                                                                     #calculate
    print("The remainder of " + str(sys.argv[1]) + " divided by 5 is " + str(mod5) + "\n")          #print remainder
    mult5 = int(mod5) * 5                                                                           #calculate
    print("The product of " + str(mod5) + " multiplied by 5 is " + str(mult5) + "\n")               #print sum
    oneLess = int(sys.argv[1]) - 1                                                                  #calculate
    print("The sum of " + str(sys.argv[1]) + " minus 1 is " + str(oneLess))                         #print sum
    return(mult5 + oneLess)                                                                         #return total

calcu()                                                         #call func
print("\n" + str(calcu()))                                      #print return as string

num1 = float((int(calcu()) + int(inputnum)) * 1.931918)         #defin var as return value and input value and number 

print("\n")                                     #Print space
print(num1)                                     #print num
print("\n")                                     #print space
print(int(num1))                                #print num as an integer
char = chr(int(num1))                           #convert num1 to a character
print("\n" + "<" + str(char) + ">")             #print char


'''
Take the command line argument, 
get the remainder when you divide it by 5, 
multiply it by 5, 
add it to the integer that is one less than itself, 
add the return value from the input function call to it, 
multiply it by 1.931918, 
convert it to an integer, 
and finally convert it to a character.
'''