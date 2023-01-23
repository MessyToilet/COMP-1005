'''
Date:           9/23/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Type conversions and arithmetic operations, from the comand line
'''

import pygame                               #Import pygame
import sys


windowSize = (480, 640)                 #Choose window size
windowColor = "White"                   #Choose bg color
windowCaption = "Assignment 1"          #choose caption text



window = pygame.display.set_mode(windowSize)            #Set up display and call it window
window.fill(windowColor)                                #Set up window color 
pygame.display.set_caption(windowCaption)               #Write caption text



while True:                                     #Main Loop
    for event in pygame.event.get():            #Check for events
        if event.type == pygame.QUIT:           #Check if users x's out
            pygame.quit()                       #Quit pygame    
            sys.exit()                          #Kill process


    pygame.display.flip()           #Update screen

