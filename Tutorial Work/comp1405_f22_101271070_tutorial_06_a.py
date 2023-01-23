'''
Date:           11/12/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Arbituary Length
'''

lis = []

while True:
    user_input = input(f"\nWhat would you like to do? \n\t1. Add Value to list. \n\t2. Remove last value from list. \n\t3. Exit loop \n")   #Print Options

    try:                                                                                                                                    #check input is int
        if int(user_input) == 1:                                                                                                            #if input is one (not sure if i have to use in() becuase 1 could be a str?)
            lis.append(input(f"\nWhat value would you like to add to your list?: "))                                                        #ask user what to add

        elif int(user_input) == 2:                                                                                                          #if input is two
            if len(lis) == 0:                                                                                                               #if list empty
                print("Your list isn't big enough...")                                                                                      #print error

            else:                                                                                                                           #and if the list isnt empty       
                lis.pop(-1)                                                                                                                 #pop last ele

        elif int(user_input) == 3:                                                                                                          #if input is three
            count = 0                                                                                                                       #define count
            for i in lis:                                                                                                                   #iterate over lis
                count += 1                                                                                                                  #count ele
            print(f"length of list is {count}.")                                                                                                                    #print count
            break                                                                                                                           #break

    except:                                                                                                                                 #if input not int
        print("\nPlease pick supported option")                                                                                             #print error
