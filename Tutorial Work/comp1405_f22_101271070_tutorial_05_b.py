'''
Date:           11/2/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Rock Paper Scissors
'''

import random

def game():                                                                         #def func
    options = ["r", "p", "s"]                                                       #def options

    Ai_option = options[random.randint(0,2)]                                        #define AI choice
    
    User_option = str(input("Pick Rock, Paper, or Scissors r/p/s: "))               #Ask for users choice

    while User_option.lower() not in ["r", "p", "s"]:                               #If user inputs invalid choice
        User_option = str(input("\nPick Rock, Paper, or Scissors r/p/s: "))         #ask again

    if User_option == Ai_option:        #if user and Ai choices are the same call a tie
        print("\nIt's a tie!")

    if User_option == "r":              #if user picked rock
        if Ai_option == "p":            #and if AI picked paper
            print("\nYou lose!")        #player lost
        elif Ai_option == "s":          #else player won
            print("\nYou win!")

    if User_option == "s":              #if user picked sicssors
        if Ai_option == "p":            #and ai picked paper
            print("\nYou win!")         #user won
        elif Ai_option == "r":          #else user lost
            print("\nYou lose!")

    if User_option == "p":              #if user picked paper
        if Ai_option == "r":            #and ai picked rock
            print("\nYou win!")         #user wins
        elif Ai_option == "s":          #else user lost
            print("\nYou lose!")


while True:                                                                       #game loop

    game()                                                                        #call fuuc

    if str(input("\n\nDo you want to keep playing?: y/n ")) == "n": break         #ask if done, if done break

print("\nThanks for playing\n\n")                                                 #print thank you

