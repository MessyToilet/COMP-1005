'''
Date:           10/19/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Pointilisim
'''
#   !   Program takes around 30-40s to finish drawing the image.

import pygame                               #Import pygame
import random                               #import random
import sys                                  #import sys

pygame.init()                               #initialize pygame

#image = pygame.image.load("C:\\Users\\jacob\\Downloads\\1carleton\\COMP 1005\\Assignments\\stockImage2.jpg")
image = pygame.image.load("C:\\Users\\jacob\\Downloads\\1carleton\\COMP 1005\\Assignments\\stockimage2.jpg")  #get src img name

(w, h) = image.get_size()                       #Get window dimensions
size = (w  * 4, h * 4)                          #calculate scaled dimensions

window = pygame.display.set_mode(size)          #Set up display and call it window 
for y in range(h):                              #go through rows
    for x in range(w):                          #go through coloumns
        (r, g, b, _) = image.get_at((x, y))     #take rgb value
        red     = int(r)    //  50               #divide by 4 to find how many dots is needed in scaled up img
        green   = int(g)    //  50              #divide by 4 to find how many dots is needed in scaled up img
        blue    = int(b)    //  50              #divide by 4 to find how many dots is needed in scaled up img
        if r < 20 and g < 20 and b < 20:                                                                                                #if the pixel is "dark"
            pygame.draw.circle(window, (10, 10, 10), (random.randint(x * 4 - 15, x * 4), random.randint(y * 4 - 15, y * 4)), 1)         #make a black circle, not pure black so it blends better
        else:                                                                                                                           #Else
            for i in range(red):                                                                                                        #repeat for every dot needed
                pygame.draw.circle(window, (255, 0, 0) , (random.randint(x * 4 - 15, x * 4), random.randint(y * 4 - 15, y * 4)), 1)     #draw colored circle
            for i in range(blue):                                                                                                       #repeat for every dot needed
                pygame.draw.circle(window, (0, 0, 255) , (random.randint(x * 4 - 15, x * 4), random.randint(y * 4 - 15, y * 4)), 1)     #draw colored circle
            for i in range(green):                                                                                                      #repeat for every dot needed
                pygame.draw.circle(window, (0, 255, 0) , (random.randint(x * 4 - 15, x * 4), random.randint(y * 4 - 15, y * 4)), 1)     #draw colored circle


while True:                                     #Main Loop
    for event in pygame.event.get():            #Check for events
        if event.type == pygame.QUIT:           #Check if users x's out
            pygame.image.save(window, "JacobChiu_101271070_2.jpg")
            pygame.quit()                       #Quit pygame    
    pygame.display.flip()                       #Update screen