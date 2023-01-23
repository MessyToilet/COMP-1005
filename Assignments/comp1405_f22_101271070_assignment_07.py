'''
Date:           11/6/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Invert image
'''

import pygame                               #Import pygame
import sys                                  #import sys

pygame.init()                               #initialize pygame

#image = pygame.image.load(sys.argv[1])
image = pygame.image.load("C:\\Users\\jacob\\Downloads\\1carleton\\COMP 1005\\Assignments\\stockimage2.jpg")

(w, h) = image.get_size()                       #Get window dimensions
size = (w, h)                                   #calculate scaled dimensions

window = pygame.display.set_mode(size)          #Set up display and call it window 

window.blit(image, (0,0))                       #blit image
while True:                                     #Main Loop
    for event in pygame.event.get():            #Check for events
        if event.type == pygame.QUIT:           #Check if users x's out
            #pygame.image.save(window, "JacobChiu_101271070.jpg")
            pygame.quit()                       #Quit pygame    

        if pygame.mouse.get_pressed()[0]:       #check if mouse is pressed
            x,y = pygame.mouse.get_pos()        #take x and y
            for i in range(50):                 #repeat 50 timez
                for k in range(50):             #repeat 50 times
                    try:                            
                        (r, g, b, _) = image.get_at((x + i - 25, y + k - 25))                               #check if pixel is in screen
                    except: 
                        pass                                                                                #stop drawing
                    pygame.Surface.set_at(window, (x + i - 25, y + k - 25), (255 - r, 255 - g, 255 - b))    #draw pixel

    pygame.display.flip()                       #Update screen