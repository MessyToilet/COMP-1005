'''
Date:           11/6/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Function Cartoon Character  -   Submmit only the funcs
'''

import pygame

windowSize = (500, 500)                             #Choose window size
win_sfc = pygame.display.set_mode(windowSize)        #Set up display and call it window
win_sfc.fill("White")                               #Set up window color 

def draw_head(x, y):
    pygame.draw.circle(win_sfc, "yellow", (x, y), 100)      #draw dot

def draw_eyes():
    centre_x = 150
    centre_y = 250
    pygame.draw.circle(win_sfc, "black", (centre_x + 40, 250), 25)      #draw dot
    pygame.draw.circle(win_sfc, "white", (centre_x + 40, 250), 22)      #draw dot - Eye Base
 
    pygame.draw.circle(win_sfc, "Black", (centre_x + 40, 245), 10)      #draw dot - Pupil

    pygame.draw.circle(win_sfc, "black", (centre_x - 40, 250), 25)      #draw dot - Eye base
    pygame.draw.circle(win_sfc, "white", (centre_x - 40, 250), 22)      #draw dot

    pygame.draw.circle(win_sfc, "Black", (centre_x - 40, 245), 10)      #draw dot - puipil

    pygame.draw.line(win_sfc, "Black", (centre_x - 70, centre_y - 40), (centre_x - 10, centre_y - 20), 5)   #draw eye brows
    pygame.draw.line(win_sfc, "Black", (centre_x + 10, centre_y - 20), (centre_x + 70, centre_y - 40), 5)   #draw eye brows

    pygame.draw.line(win_sfc, "Black", (centre_x + 40 + 20, centre_y + 10), (centre_x + 40 - 20, centre_y + 10), 3)   #Draw eyelid
    pygame.draw.line(win_sfc, "Black", (centre_x - 40 - 20, centre_y + 10), (centre_x - 40 + 20, centre_y + 10), 3)   #Draw eyelid
     

def draw_hat():
    centre_x = 450
    centre_y = 350

    pygame.draw.rect(win_sfc, "black", pygame.Rect(centre_x - 50, centre_y - 250, 100, 150)) #top part
    pygame.draw.rect(win_sfc, "black", pygame.Rect(centre_x - 100, centre_y - 100, 200, 50)) #bottom part

    pygame.draw.rect(win_sfc, "white", pygame.Rect(centre_x - 45, centre_y - 160, 90, 15)) #white strap
    pygame.draw.rect(win_sfc, "white", pygame.Rect(centre_x - 45, centre_y - 130, 90, 15)) #white strap
    pygame.draw.circle(win_sfc, "yellow", (centre_x, centre_y - 137), 25)      #draw coin

    return("top hat")

def draw_mouth(x, y):
    centre_x = x 
    centre_y = y 

    pygame.draw.ellipse(win_sfc, "black", pygame.Rect(centre_x - 50, centre_y + 25, 100, 50)) #outline
    pygame.draw.ellipse(win_sfc, "red", pygame.Rect(centre_x - 40, centre_y + 30, 80, 40))  #mouth

    pygame.draw.circle(win_sfc, "white", (centre_x, centre_y + 35), 5)      #draw teeth
    pygame.draw.circle(win_sfc, "white", (centre_x, centre_y + 65), 5)      #draw teeth

    pygame.draw.circle(win_sfc, "white", (centre_x - 10, centre_y + 35), 5)      #draw teeth
    pygame.draw.circle(win_sfc, "white", (centre_x - 10, centre_y + 65), 5)      #draw teeth

    pygame.draw.circle(win_sfc, "white", (centre_x + 10, centre_y + 35), 5)      #draw teeth
    pygame.draw.circle(win_sfc, "white", (centre_x + 10, centre_y + 65), 5)      #draw teeth

    pygame.draw.circle(win_sfc, "white", (centre_x + 20, centre_y + 37), 5)      #draw teeth
    pygame.draw.circle(win_sfc, "white", (centre_x + 20, centre_y + 62), 5)      #draw teeth

    pygame.draw.circle(win_sfc, "white", (centre_x - 20, centre_y + 37), 5)      #draw teeth
    pygame.draw.circle(win_sfc, "white", (centre_x - 20, centre_y + 62), 5)      #draw teeth

    pygame.draw.circle(win_sfc, "white", (centre_x - 30, centre_y + 40), 5)      #draw teeth
    pygame.draw.circle(win_sfc, "white", (centre_x - 30, centre_y + 60), 5)      #draw teeth

    pygame.draw.circle(win_sfc, "white", (centre_x + 30, centre_y + 40), 5)      #draw teeth
    pygame.draw.circle(win_sfc, "white", (centre_x + 30, centre_y + 60), 5)      #draw teeth


while True:    
    
    draw_eyes()
    draw_hat()
    draw_mouth(300,300)
                                     #Main Loop
    for event in pygame.event.get():            #Check for events
        if event.type == pygame.QUIT:           #Check if users x's out
            pygame.quit()                       #Quit pygame    



    pygame.display.flip()           #Update screen

