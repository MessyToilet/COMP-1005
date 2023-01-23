'''
Date:           10/19/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Guess the number
'''

import random 
nums = [int(input("pick a number from 1 - 100: ")), random.randint(1, 100), 10]
while nums[0] != nums[1] and nums[2] > 0:
    if nums[0] > nums[1] : nums[0] = int(input("Your number was too big \nPick a number between 1 - 100: "))
    else : 
        nums[0] = int(input("Your number was too small \nPick a number between 1 - 100: "))
        nums[2] -= 1
if nums[2] == 0 : print("You ran out of trys")
else : print("You got it!")