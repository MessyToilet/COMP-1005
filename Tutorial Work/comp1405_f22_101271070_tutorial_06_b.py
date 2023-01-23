'''
Date:           11/12/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Replacing and counting
'''
import random

lis = []                                        #set empty list

n_integers = int(input(f"Pick n integer: "))    #define user input

for i in range(n_integers):                     #loop n_integers times
    lis.append(random.randint(1, n_integers))   #append a random num

#print(lis)

def change(list):                                                               #def func
    user_input_number = int(input(f"What number are you looking for? "))        #define user input
    user_input_word = input(f"What shall we replace it with? ")                 #define user input
    for index, ele in enumerate(list):                                          #enumerate over list
        if ele == user_input_number:                                            #if ele in list is the same as input
            list.pop(index)                                                     #remove that ele
            list.insert(index, user_input_word)                                 #replace that ele
    return(list)

def counter(list, string):                                                      #def func
    count = 0                                                                   #set count to 0
    for i in list:                                                              #iterate over list
        if i == string:                                                         #if ele is equal to parameter
            count += 1                                                          #count
    return(count)                                                               #return count

print(counter(change(lis), str(input(f"What string do you want to count? (case sensitive) "))))
#print - return of counter when the return of change lis is passed, along with user input
