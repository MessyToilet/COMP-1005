'''
Date:           11/23/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    reading tile mapping files
'''

import pygame                   #Import pygame              
import sys

def better_main():
    while True:
        try:
            FILE_NAME = str(input("ENTER FILE NAME: "))
            with open(FILE_NAME) as FILE:
                break
        except:
            print("ERROR, INVALID FILE NAME GIVEN.")

    with open(FILE_NAME) as FILE:
        (file_x_len, file_y_len), IMGS = (len(FILE.readline().strip("\n")), sum(1 for line in FILE) + 1), []
        FILE.seek(0, 0)
        for i in range(5):
            while True:
                try:
                    IMG = str(input(f"ENTER FILE NAME FOR IMAGE {i}: "))
                    loaded_img = pygame.image.load(IMG)
                    IMGS.append(IMG)
                    break
                except : print("ERROR, IMAGE NOT FOUND.")

        (DISP_WIDTH, DISP_HEIGHT) = loaded_img.get_size()
        pygame.init()
        window, blitz_x, blitz_y = pygame.display.set_mode((DISP_WIDTH * file_x_len, DISP_HEIGHT * file_y_len)), 0, 0 

       
        for LINE in FILE:
            for chr in LINE.strip("\n"):
                try : int(chr)                   
                except:
                    print("ERROR, NON INTEGER TYPE FOUND IN FILE.")
                    return

                window.blit(pygame.image.load(IMGS[int(chr)]), (blitz_x, blitz_y))
                blitz_x += DISP_WIDTH                              #increase x by image width
            blitz_y, blitz_x = blitz_y + DISP_HEIGHT, 0                                 #increase y

    while True:                                                #Main Loop
        for event in pygame.event.get():                       #Check for events
            if event.type == pygame.QUIT:                      #Check if users x's out
                #pygame.image.save(window, "JacobChiu_101271070.jpg")
                pygame.quit()                                  #Quit pygame
                sys.exit()                                         
        pygame.display.flip()                                  #Update screen

better_main()


def main():                     #define main func
    loading_images = True       #set flag true
    while loading_images:       #while flag true
        try:
            image_0 = pygame.image.load(str(input("PLEASE INPUT FILE NAME FOR IMAGE 0: ")))     #ask for image file
            image_1 = pygame.image.load(str(input("PLEASE INPUT FILE NAME FOR IMAGE 1: ")))     #ask for image file
            image_2 = pygame.image.load(str(input("PLEASE INPUT FILE NAME FOR IMAGE 2: ")))     #ask for image file
            image_3 = pygame.image.load(str(input("PLEASE INPUT FILE NAME FOR IMAGE 3: ")))     #ask for image file
            image_4 = pygame.image.load(str(input("PLEASE INPUT FILE NAME FOR IMAGE 4: ")))     #ask for image file
            loading_images = False                                                              #if test passed, change flag value
        except:                                                                                 #if test failed
            print("IMAGE FILE CANNOT BE FOUND...")                                              #print error

    while True:                                         #while user is choosing a file
        FILE_NAME = str(input("ENTER FILE NAME: "))     #ask for a file name
        try:                                            #try
            FILE = open(FILE_NAME, "r")                 #see if the file exists, if it does
            break                                       #break
        except:                                         #except
            print("\nFILE not found...")                #print error
    graph_length = 0
    for line in FILE:                                                       #for line in file
        graph_width = 0                                                     #set var to 0
        for chr in line.strip("\n"):                                        #for characters in line, strip new line character
            if (ord(chr) >= 48 and ord(chr) <= 57):                         #if ascii val is valid
                graph_width+= 1                                             #increase graph width, because we can't use len?
            else:                                                           #if anything but a pos int is found
                print("NON INTEGER TYPE FOUND IN FILE, TERMINATING...")     #print error
                return                                                      #end func
        graph_length += 1   
                                        #increase graph len (rows)
    FILE.close()                                                            #close the file

    graph = []                              #set graph to be empty lis
    for i in range(graph_length):           #repeat for rows in matrix
        graph.append([])                    #append empty lis for each row

    FILE = open(FILE_NAME, "r")             #open file
    for i in range(graph_length):           #repeat graph len times
        data = FILE.readline()              #data is the line in the file
        for k in range(graph_width):        #repeat graph width time (to avoid new line chr)
            graph[i].append(data[k])        #append the chr into graph
    FILE.close()                            #close

    for row in graph:                                               #iterate over graph
        for num in row:                                             #iterate over row, iterating over graph
            if (int(num) < 0) or (int(num) > 4):                    #if unsupported num is found (could intergrat this with above code)
                print("UN SUPPORTED IMAGE VALUE, TERMINATING...")   #print error
                return                                              #break out of func
    
    pygame.init()                                                       #init pygame

    (image_width, image_height) = image_0.get_size()                    #get x, y size of image
    display_width = image_width * graph_width                           #set display size to proper size
    display_length = image_height * graph_length                        #set display size to proper size, this is to insure that display size is relevent to image size 

    window = pygame.display.set_mode((display_width, display_length))   #set up window with proper size

    blitz_x = 0                                                 #set x val
    blitz_y = 0                                                 #set y val
    for i in range(graph_length):                               #iterate for graph length
        for k in range(graph_width):                            #iterate for graph width
            if graph[i][k] == "0":                              #if graph code is 0
                window.blit(image_0, (blitz_x, blitz_y))        #blitz corresponding image
                
            if graph[i][k] == "1":                              #if graph code is 1
                window.blit(image_1, (blitz_x, blitz_y))        #blitz corresponding image
                
            if graph[i][k] == "2":                              #if graph code is 2
                window.blit(image_2, (blitz_x, blitz_y))        #blitz corresponding image
                
            if graph[i][k] == "3":                              #if graph code is 3
                window.blit(image_3, (blitz_x, blitz_y))        #blitz corresponding image
                
            if graph[i][k] == "4":                              #if graph code is 4
                window.blit(image_4, (blitz_x, blitz_y))        #blitz corresponding image

            blitz_x += image_width                              #increase x by image width

            if blitz_x >= display_width:                        #if x is greater than display size
                blitz_x = 0                                    #reset x
                blitz_y += image_height                        #increase y

    while True:                                                #Main Loop
        for event in pygame.event.get():                       #Check for events
            if event.type == pygame.QUIT:                      #Check if users x's out
                #pygame.image.save(window, "JacobChiu_101271070.jpg")
                pygame.quit()                                  #Quit pygame
                sys.exit()                                         
        pygame.display.flip()                                  #Update screen

#main()      #call main

