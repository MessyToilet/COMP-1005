'''
Date:           11/30/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Bogosort and Bozosort
'''

import random                                           #import random

def insertionsort(list_arg):                            #def func, pass lis - From tutorial
    new_list = []                                       #set new list
    for i in range(len(list_arg)):                      #repeat for length of list
        new_list.append(list_arg[i])                    #create a new list
    for i in range(1, len(new_list)):                   #repeat for length of new list, start at 1
        j = i                                           #set j = i
        while j > 0 and new_list[j-1] > new_list[j]:    #while j greater than 0 and the tested ele is greater than the curent ele
            list_arg = swap(new_list, j, (j - 1))       #swap the eles
            j -= 1                                      #reduce j
    return new_list                                     #return list

def swap(list_arg, i, j):                                   #def func, pass lis, and two indexs
    list_arg[i], list_arg[j] = list_arg[j], list_arg[i]     #swap the value at positions j and i
    return list_arg                                         #return list

def bogosort(lis, ans):             #def func, pass lis and answer
    new_list1 = []                  #set new list
    for i in range(len(lis)):       #repeat for lenght of list
        new_list1.append(lis[i])    #create new list
    while True:                     #while true
        if new_list1 == ans:        #if new list is sorted
            #return(new_list1)
            return(True)            #return true
        else:                                                   #else
            for i in range(len(new_list1)):                     #repeat for length of list
                index = random.randint(0, len(new_list1) - 1)   #pick random index
                new_list1 = swap(new_list1, index, i)           #swap random index with i

def bozosort(lis, ans):             #def func, pass list an answer
    new_list2 = []                  #set new list
    for i in range(len(lis)):       #repeat for length of list
        new_list2.append(lis[i])    #create new list
    while True:                     #while true
        if new_list2 == ans:        #if new list is sorted
            #return(new_list2)
            return(True)            #return true
        else:                       #else
            #print("doing")
            index1 = random.randint(0, len(lis) - 1)                                        #pick random index
            index2 = random.randint(0, len(lis) - 1)                                        #pick random index
            new_list2[index1], new_list2[index2] = new_list2[index2], new_list2[index1]     #swap them

def main():                                                                             #def main
    while True:                                                                         #while true
        try:                                                                            #try
            list_length = int(input("Enter an integer for length of list: "))           #ask for length 
            break                                                                       #break
        except:                     #except
            print("Try Again")      #print error
    while True:                     #while true
        try:                                                                                #try
            list_max = int(input("Enter an integer for the max value of the list: "))       #ask for max value
            break                                                                           #break
        except:                                     #except
            print("Try Again")                      #print error
    list = []                                       #set new list
    for i in range(list_length):                    #create list with same length given
        list.append(random.randint(1, list_max))    #fill with random numbers from give
    print()                                         #print space
    print(list, "Original")                         #print the original list        
    answer = insertionsort(list)                    #determine the sorted list
    print(answer, "Insertion sort")                 #print the sorted list
    print(bogosort(list, answer), "Bogosort")       #print return from bogosort
    print(bozosort(list, answer), "Bozosort")       #print return from bozosort
    return                                          #end func

main()                                              #call main

"""
BOGOSORT

Given:  List

Take list
Randomly rearrange list
Check if list is in order

If yes, Stop

else, repeat
"""

"""
BOZOSORT

Given: List

Take two random points in list
check if which ele is bigger
swap eles (if eles are not the same)

contiune process until the list is sorted
"""
