'''
Date:           11/30/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Emperical Performance Analysis
'''

import random                                           #import random
import time

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
            #print(new_list1)
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
            #print(new_list2)
            return(True)            #return true
        else:                       #else
            #print("doing")
            index1 = random.randint(0, len(lis) - 1)                                        #pick random index
            index2 = random.randint(0, len(lis) - 1)                                        #pick random index
            new_list2[index1], new_list2[index2] = new_list2[index2], new_list2[index1]     #swap them

def Empirical_Performance_Analysis(func):                                       #def func
    average = []                                                                #create random list
    for i in range(5):                                                          #repeat 5 times
        lis = [random.randint(1, 10) for i in range(random.randint(5, 10))]     #create random list
        #print(lis) 
        start = time.time()                                                     #collect start time
        func(lis, insertionsort(lis))                                           #call func and pass the ans
        end = time.time() - start                                               #determine end time
        average.append(end)                                                     #append the end time
    return(sum(average) / len(average))                                         #return the average

def main():                                         #def main
    list = []                                       #set new list                      
    for i in range(random.randint(5,10)):           #create list with same length given
        list.append(random.randint(1, 10))          #fill with random numbers from give
    #print(list)
    print("On average, Bogosort took:", Empirical_Performance_Analysis(bogosort), "seconds.")       #Call func, pass params
    print("On average, Bozosort took:", Empirical_Performance_Analysis(bozosort), "seconds.")       #call func, pass params 
    return                                          #end func

main()                                              #call main