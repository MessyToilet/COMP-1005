'''
Date:           9/17/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Re-create shapes from email with pygame
'''


import pygame                               #Import pygame


windowSize = (480, 640)                 #Choose window size
windowColor = "White"                   #Choose bg color
windowCaption = "Assignment 1"          #choose caption text


window = pygame.display.set_mode(windowSize)            #Set up display and call it window
window.fill(windowColor)                                #Set up window color 
pygame.display.set_caption(windowCaption)               #Write caption text

     
poly1 = [(166, 65, 77), ((0,0),(240,0),(180,90),(0,90))]                                    #Set color for poly1, and list all points 
poly2 = [(200, 107, 54), ((240, 0), (240, 200), (300, 100), (400, 100), (400, 0))]            #Set color for poly2, and list all points 


pygame.draw.polygon(window, poly1[0], poly1[1])         #Create poly1, draw on window and use data in poly1 list
pygame.draw.polygon(window, poly2[0], poly2[1])         #Create poly2, draw on window and use data in poly2 list


while True:                                     #Main Loop
    for event in pygame.event.get():            #Check for events
        if event.type == pygame.QUIT:           #Check if users x's out
            pygame.quit()                       #Quit pygame    
    pygame.display.flip()                       #Update screen


'''
https://www.petercollingridge.co.uk/tutorials/pygame-physics-simulation/creating-pygame-window/
https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_Languages/Book%3A_Making_Games_with_Python_and_Pygame_(Sweigart)/03%3A_Pygame_Basics/3.06%3A_The_QUIT_Event_and_pygame.quit()_Function
Used to help create Main Loop
'''

