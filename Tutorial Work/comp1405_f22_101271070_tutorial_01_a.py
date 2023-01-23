'''
Date:           9/23/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Draw "The Swan" using draw.arc and draw.rect
'''

import pygame                               #Import pygame



windowSize = (300, 300)                 #Choose window size
windowColor = "White"                   #Choose bg color
windowCaption = "Tutorial 1"          #choose caption text

window = pygame.display.set_mode(windowSize)            #Set up display and call it window
window.fill(windowColor)                                #Set up window color 
pygame.display.set_caption(windowCaption)               #Write caption text


orange = (157, 60, 41)      #define color

white = (209, 201, 195)     #define color

black = (32, 32, 32)        #define color

blue = (84, 126, 183)       #define color

yellow = (220, 184, 83)     #define color

pink= (219, 117, 85)        #define color

pygame.draw.rect(window, orange, (0, 0, 300,300))       #draw rectangle

pygame.draw.rect(window, pink, (75,75,150,150))
pygame.draw.arc(window, white, (75,75,150,150), 1.57, 4.71, width = 100)    #draw semi cirlce

pygame.draw.arc(window, blue, (75,75,150,150), 4.71, 1.57, width = 100)     #draw semi circle

pygame.draw.rect(window, pink, (96,96, 110, 110))

pygame.draw.arc(window, black, (96,96, 110, 110), 1.57, 4.71, width = 100)  #draw semi circle
pygame.draw.arc(window, yellow, (95,95, 111, 111), 4.71, 1.57, width = 100) #draw semi circke

pygame.draw.rect(window, pink, (112,112, 77, 77))
pygame.draw.arc(window, pink, (112,112, 77, 77), 4.71, 1.57, width = 100)   #draw semi sircle

while True:                                     #Main Loop
    for event in pygame.event.get():            #Check for events
        if event.type == pygame.QUIT:           #Check if users x's out
            pygame.quit()                       #Quit pygame    
    pygame.display.flip()                       #Update screen
