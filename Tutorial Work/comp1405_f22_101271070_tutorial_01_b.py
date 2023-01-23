'''
Date:           9/23/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    "Style 1305" recreate the figures and give them props
'''

import pygame                               #Import pygame


windowSize = (600, 600)                 #Choose window size
windowColor = "White"                   #Choose bg color
windowCaption = "Tutorial 1"            #choose caption text

window = pygame.display.set_mode(windowSize)            #Set up display and call it window
window.fill(windowColor)                                #Set up window color 
pygame.display.set_caption(windowCaption)               #Write caption text

pygame.draw.rect(window, "blue", (300,300, 20, 20))

def drawPerson(x, y):
    tempy = y
    #draw body
    pygame.draw.polygon(window, "black", ((x, y), (x + 20, y), (x + 20, y + 30), (x, y + 30)))  

    #draw shoulders
    pygame.draw.circle(window, "black",(x + 10, y), 10, width=10)

    #draw head
    pygame.draw.circle(window, "black", (x + 10, y - 25), 10, width=10)

    #draw arms
    #pygame.draw.rect(window, "blue", ((x + 15),y - 10,(30),(25)))
    pygame.draw.arc(window, "black",((x + 15),y - 15,(30),(25)), 3.14, 6.28, width = 5)

    #pygame.draw.rect(window, "blue", (x - 27,y - 15, 35, 25))
    pygame.draw.arc(window, "black",((x - 27,y - 15, 35, 25)), 3.14, 6.28, width = 5)

    #draw legs
    #pygame.draw.rect(window, "blue",  (x-20, y+23, 35, 35))
    pygame.draw.arc(window, "black",((x-15, y+23, 35, 35)), 0.78, 3.92, width = 5)
    #pygame.draw.rect(window, "blue",  (x+15, y+23, 35, 35))
    pygame.draw.arc(window, "black",((x, y+23, 35, 35)), 5.49, 2.35, width = 5)

    #draw stress lines
    pygame.draw.line(window, "red", (x + 25,y-27), (x+ 30, y - 27), width = 3)
    pygame.draw.line(window, "red", (x + 23,y-35), (x+ 27, y - 37), width = 3)
    pygame.draw.line(window, "red", (x + 17,y-40), (x+ 20, y - 45), width = 3)

    #draw feet
    pygame.draw.line(window, "black", (x - 20,y+50), (x- 10, y + 50), width = 3)
    pygame.draw.line(window, "black", (x + 30,y+50), (x+ 40, y + 50), width = 3)
    
    #draw hands
    pygame.draw.circle(window, "black", (x + 44,y-2),5, width = 6)
    pygame.draw.circle(window, "black", (x - 27,y-2),5, width = 6)

    #draw ball
    pygame.draw.circle(window, "red", (x + 50,y-10),10, width = 10)

    #draw smile
    pygame.draw.arc(window, "white", (x-21,y-32, 30, 20), 3.14, 6.28, width=1)
    #draw eye
    pygame.draw.circle(window, "white", (x + 6,y-29),2, width = 2)
    #draw eye
    pygame.draw.circle(window, "black", (x -1,y-31),2, width = 2)
    #draw line
    pygame.draw.line(window, "black", (x,y-23), (x-5,y-23), width = 3)


drawPerson(300,300) #call draw person, pass coordinants 

while True:                                     #Main Loop
    for event in pygame.event.get():            #Check for events
        if event.type == pygame.QUIT:           #Check if users x's out
            pygame.quit()                       #Quit pygame    
    pygame.display.flip()           #Update screen
