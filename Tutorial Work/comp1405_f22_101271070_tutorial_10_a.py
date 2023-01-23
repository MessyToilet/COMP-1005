'''
Date:           12/5/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Recursive Design Practice I
'''

def iterative(lis):                                         #def func
    if type(lis) != list:                                   #check type
        print("Iteratve func was given a non list value")   #print error
        return                                              #end func

    for i in range(len(lis)):                               #iterate through lis
        if lis[i] % 2 != 0:                                 #if ele is odd
            lis[i] = lis[i] + 10                            #increase ele by 10
    return lis                                              #return lis

def recursive(lis):                                         #def rec func
    if type(lis) != list:                                   #check type
        print("Recursive func was given a non list value")  #print error
        return                                              #return
        
    if len(lis) == 0:                                       #if len is 0 (base case)
        return lis                                          #return lis

    if lis[0] % 2 != 0:                                     #if ele is odd
        lis[0] = lis[0] + 10                                #increase ele by 10

    return lis[:1] + recursive(lis[1::])                    #return the first ele of the lis plus the return of the next func

lis = [x for x in range(10)]        #make lis                            
lis2 = [x for x in range(10)]       #make identical lis

print(lis)                          #print lis

print(iterative(lis))               #print return
print(recursive(lis2))              #print return
