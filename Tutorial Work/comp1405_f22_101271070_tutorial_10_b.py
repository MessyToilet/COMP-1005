'''
Date:           12/5/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Recursive Design Practice II
'''

def iterative(lis):                                         #def func
    if type(lis) != list:                                   #check type
        print("Iteratve func was given a non list value")   #print error
        return                                              #end func

    for i in range(len(lis)):                               #iterate through lis
        if ord(lis[i]) == 97 or ord(lis[i]) == 101 or  ord(lis[i]) == 105 or ord(lis[i]) == 111 or ord(lis[i]) == 117:      #if chr is a vowel                                
            lis[i] = chr(ord(lis[i]) - 32)                                                                                  #make it uppercase
    return lis                                              #return lis

def recursive(lis):                                         #def rec func
    if type(lis) != list:                                   #check type
        print("Recursive func was given a non list value")  #print error
        return                                              #return
        
    if len(lis) == 0:                                       #if len is 0 (base case)
        return lis                                          #return lis

    if ord(lis[0]) == 97 or ord(lis[0]) == 101 or  ord(lis[0]) == 105 or ord(lis[0]) == 111 or ord(lis[0]) == 117:          #if chr is a vowel                            
        lis[0] = chr(ord(lis[0]) - 32)                                                                                      #make it uppercase

    return lis[:1] + recursive(lis[1::])        #return the first ele of the lis plus the return of the next func

lis = [chr(x) for x in range(97, 123)]          #make lis                            
lis2 = [chr(x) for x in range(97, 123)]         #make identical lis

print(lis)                   #print lis
print()                      #print space
# print(ord("a"))
# print(ord("z"))
# print(ord("A"))

# print(ord("a"))
# print(ord("e"))
# print(ord("i"))
# print(ord("o"))
# print(ord("u"))

print(iterative(lis))       #print return
print()                     #print space
print(recursive(lis2))      #print return