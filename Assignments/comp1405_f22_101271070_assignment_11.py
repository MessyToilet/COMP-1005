'''
Date:           12/3/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Type conversions and arithmetic operations, from the comand line
'''

import pygame                           #Import pygame
import sys                              #import Sys
import random                           #import random
import time                             #Import time

pygame.init()                           #initialize pygame

windowSize = (900, 900)                 #Choose window size
windowColor = "black"                   #Choose bg color
windowCaption = "Assignment 1"          #choose caption text

while True:                                                                 #while true
    if str(input("Resume or Start from beginning? r/b ")).upper() == "B":
        try:                                                                #try
            FILE = open("pogo.txt", "r")                                    #open default file
            break                                                           #break
        except:                                                         #except
            try:                                                        #try
                FILE = open(str(input("\nFILE NAME: ")), "r")           #open user given file
                break                                                   #break
            except:                                                     #except
                print("\nFile could not be found.")                     #print error
    else:                                                               #else
        try:                                                            #try
            FILE = open("pogo2.txt")                                    #open the new file
            break                                                       #break
        except:                                                         #except
            try:                                                        #try
                FILE = open(str(input("\nFILE NAME: ")), "r")           #open user given file
                break                                                   #break
            except:                                                     #except
                print("\nFile could not be found.")                     #print error

def create_stars():                                             #def func
    background = pygame.display.set_mode(windowSize)            #Set up display and call it window
    background.fill(windowColor)                                #Set up window color

    for i in range(60):                                                                                 #repeat 60 times
        pygame.draw.circle(background, "white", (random.randint(1, 900), random.randint(1, 900)), 2)    #draw stars


text_window = pygame.display.set_mode(windowSize)           #set text window
font = pygame.font.SysFont( "Arial", 50)                    #create font                                    
font = font.render("TEMP", True, "white")                   #create font

all_text = []                                               #set text list

for line in FILE:                                           #iterate through file
    all_text.append(line.strip("\n"))                       #append each line

FILE.close()


size = 50

for i in range(len(all_text)):                              #repeat for len of the file
    #print()                                                #print space
    create_stars()                                          #create stars
    #time.sleep(.25)                                        #sleep
    pygame.time.wait(500)

    for k in range(i, -1, -1):                              #repeat for i, counting backwards                                                               
        #print(size, k, all_text[k])                         
        y_pos = (850 - (( -k * 50) + (i * 50) ))            #set y pos

        if y_pos % 100 == 0:                                #if y pos is 100, 200, ...
            scaling_factor = y_pos // 50                    #divide y pos by 50
            size = size - (scaling_factor) // 2             #change size to be size minus scaling factor minus 2

        elif y_pos == 900:                                          #if word if off screen
            all_text.pop(0)                                         #pop that word

        font = pygame.font.SysFont( "Arial", size)                  #set pygame font                                               #create font   
        font = font.render(all_text[k], True, "yellow")             #render font                                                #create font
        FONT_RECT = font.get_rect(center=(((900 / 2), y_pos)))      #set area                                       #set area of text
        text_window.blit(font, FONT_RECT)                           #blit text                                             #blits text

        for event in pygame.event.get():            #Check for events
            if event.type == pygame.QUIT:           #Check if users x's out
                FILE = open("pogo2.txt", "w")       #open/ create a new file
                for text in all_text[i::]:          #iterate through un-used word
                    FILE.write(str(text + "\n"))    #add word
                pygame.quit()                       #Quit pygame    
                sys.exit()                          #Kill process
        
    size = 50                                       #reset size
    
    pygame.display.flip()                           #Update screen
