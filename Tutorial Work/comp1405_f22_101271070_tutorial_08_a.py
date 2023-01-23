'''
Date:           11/23/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Writing Tile Maps
'''

import random

def main():

    
    file_exists     = False                             #set flag variable
    while True:                                #while user is choosing a file
        FILE_NAME = str(input("ENTER FILE NAME: "))     #ask for a file name
        try:                                            #try
            open(FILE_NAME, "r")                        #see if the file exists
        except:                                         #except
            FILE = open(FILE_NAME, "w")                 #create a new file
            break

        file_exists = True                              #change flag variable (enters if statement) (this is needed because the loop doesn't break after cycling and we want to avoid the if statment)
        if file_exists == True and str(input("\nTHIS FILE ALREADY EXISTS... \nDO YOU WISH TO OVERWRITE THE FILE?: \ny/n ")).upper() in ["Y", "YES"]:
                                                        #if the program found a file with same name and user wants to overwrite the file
            FILE = open(FILE_NAME, "w")                 #overwrite the file
            break

    map_width   = int(input("\nHOW MANY TILES WIDE WOULD YOU LIKE YOUR MAP?:\n"))       #ask user for width, since we don't know the size of the images use image itself as metric
    map_height  = int(input("\nHOW MANY TILES TALL WOULD YOU LIKE YOUR MAP?:\n"))       #ask user for width, since we don't know the size of the images use image itself as metric

    Image_0 = str(input("WHICH IMAGE WOULD YOU LIKE TO ASSIGN TO IMAGE 0? "))           #assign image with user input
    Image_1 = str(input("WHICH IMAGE WOULD YOU LIKE TO ASSIGN TO IMAGE 1? "))           #assign image with user input
    Image_2 = str(input("WHICH IMAGE WOULD YOU LIKE TO ASSIGN TO IMAGE 2? "))           #assign image with user input
    Image_3 = str(input("WHICH IMAGE WOULD YOU LIKE TO ASSIGN TO IMAGE 3? "))           #assign image with user input
    Image_4 = str(input("WHICH IMAGE WOULD YOU LIKE TO ASSIGN TO IMAGE 4? "))           #assign image with user input

    map =[]                         #set empty graph

    for i in range(map_height):     #append rows into graph (map_height times)
        map.append([])              #append empty list

    for i in range(map_width):                      #for map width times
        for k in range(map_height):                 #and for map height times
            map[i].append(random.randint(0 , 4))    #append a random data entry

    for row in map:                                 #repeat for each row
        for ele in row:                             #grab each ele in the graph row
            FILE.write(str(ele))                    #write it to the file
        FILE.write("\n")                            #start next line

    FILE.close()

main()