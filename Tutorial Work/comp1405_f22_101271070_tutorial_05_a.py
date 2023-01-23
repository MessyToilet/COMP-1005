'''
Date:           11/2/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Prmie Numbers
'''


def isprime(num):                       #create func
    if num == 1 : return(True)          #if num is 1 return true
    if num == 2 : return(False)         #if num is 2 return false
    for i in range(2, int(num - 1)):    #starting at two go until one less
        if num % i == 0:                #if num is divisible by any num lesser
            return(True)                #return true
    return(False)                       #else return false
            
guesing = True                          #set true

while guesing:                                  #while true
    num = float(input("Pick a number: "))       #take a num

    if isprime(num) == True:                    #call func and check
        print("Is not prime")                   #if not prime tell user
    else:
        print("Is prime")                       #else tell user num is prime

    if str(input("Are you done? y/n ")) in ["y", "Y"]:  #ask if user is done
        guesing = False                                 #if yes than break

