'''
Date:           11/12/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Adjacency List / Game
'''

import pygame       #import pygame
import sys          #import sys
import time         #import time

pygame.init()       #init pygame         

while True:         #while ture
    try:                                        #try
        image = pygame.image.load("MAP1.gif")   #search for file
        break                                   #break
    except:                                     #except
        print("\nMAP.gif Could not be found.")  #print error
        while True:                             #while true
            try:                                                        #try
                image = pygame.image.load(str(input('\nFILE NAME: ')))  #ask for file name
                break                                                   #break
            except:                                                     #except
                print("\nFile could not be found.")                     #print error
            
    break                                                               #break


window = pygame.display.set_mode((1000,1000))           #set up window
DEFULAT_IMG_SZ = (1000, 1000)                           #set img size
image = pygame.transform.scale(image, DEFULAT_IMG_SZ)   #scale img
pygame.Surface.blit(window, image, (0,0))               #blit img
pygame.display.flip()                                   #Update screen      

'''
KEY

ROOM 0      -   Pantry room 
ROOM 1      -   Storage room 
ROOM 2      -   Inner Foyer
ROOM 3      -   Second Dining Room
ROOM 4      -   Guest Room
ROOM 5      -   Kitchen
ROOM 6      -   Outer Foyer
ROOM 7      -   Guest Room
ROOM 8      -   Second Guest Room
ROOM 9      -   Living room
ROOM 10     -   Master bedroom
ROOM 11     -   Second Master Bedroom
ROOM 12     -   bedroom
ROOM 13     -   second bedroom
ROOM 14     -   Garage
ROOM 15     -   Master Bedroom Hallway
ROOM 16     -   Bedroom Hallway
ROOM 17     -   second bedrooms closet
ROOM 18     -   bedrooms closet
ROOM 19     -   storage hallway
ROOM 20     -   Hallway


'''

ADJACENCY_LIST = [          #graph

    [3],                    #   0
    [19],                   #   1
    [4, 6],                 #   2
    [0, 7, 19],             #   3
    [2, 19],                #   4
    [6, 9, 20],             #   5
    [2, 5, 16],             #   6
    [3, 20],                #   7
    [9],                    #   8
    [5, 8, 15],             #   9
    [15],                   #   10
    [15],                   #   11
    [16, 17],               #   12
    [16, 18],               #   13
    [16],                   #   14
    [9, 10, 11],            #   15
    [6, 12, 13, 14],        #   16
    [12],                   #   17
    [13],                   #   18
    [1, 3, 4],              #   19
    [5, 7, 9]               #   20

]

DIRECTIONS = [                              #directional key words

    ["SOUTH"],                              #   0
    ["SOUTH"],                              #   1
    ["SOUTH", "EAST"],                      #   2
    ["NORTH", "SOUTH", "EAST"],             #   3
    ["NORTH", "WEST"],                      #   4
    ["NORTH", "SOUTH", "WEST"],             #   5
    ["WEST", "SOUTH", "EAST"],              #   6
    ["NORTH", "EAST"],                      #   7
    ["EAST"],                               #   8
    ["NORTH", "WEST", "SOUTH"],             #   9
    ["EAST"],                               #   10
    ["WEST"],                               #   11
    ["NORTH", "SOUTH"],                     #   12
    ["SOUTH", "NORTH"],                     #   13
    ["NORTH"],                              #   14
    ["NORTH", "WEST", "EAST"],              #   15
    ["WEST", "EAST", "NORTH", "SOUTH"],     #   16
    ["NORTH"],                              #   17
    ["SOUTH"],                              #   18
    ["NORTH", "WEST", "SOUTH"],             #   19
    ["EAST", "WEST", "SOUTH"]               #   20

]

NAMES = [                                   #Names of areas


   "Pantry room",           
   "Storage room",
   "Inner Foyer",
   "Second Dining Room",
   "Guest Room",
   "Kitchen",
   "Outer Foyer",
   "second Guest Room",
   "third Guest Room",
   "Living room",
   "Master bedroom",
   "Second Master Bedroom",
   "bedroom",
   "second bedroom",
   "Garage",
   "Master Bedroom Hallway",
   "Bedroom Hallway",
   "second bedrooms closet",
   "bedrooms closet",
   "Washroom",
   "Hallway"

]

DESCRIPTIONS = [ #game messeges

   "This looks like a pantry room, they have alot of free costco samples saved up...",
   "This looks like a storage room, it's almost empty...",
   "This must be the Inner Foyer, why's the funiture all DYI.",
   "This must be the Second Dining Room, the paint is stripping.",
   "This looks like a Guest Room, those bedsheets look crusty.",
   "You're in the Kitchen, they have one set of cutlery per person (3).",
   "You're in the Outer Foyer, there are dollarama shoes are lined up (6).",
   "You're in a second Guest Room, these bedsheets look fine.",
   "This is a third Guest Room, this one has a TV.",
   "This looks like the Living room, theres envelopes on the table.",
   "You're in the Master bedroom, wait it's just a mattress on the ground?",
   "This looks like the Second Master Bedroom, theres a sleeping bag where a bed would be.",
   "you're in the bedroom, theres a cardboard box being used as a table.",
   "you're in the second bedroom, theres abound of newspapers sewn together as a blanket.",
   "This looks like the Garage, theres a bucket on the ground...",
   "You're in the Master Bedroom Hallway, theres a family photo on the wall...",
   "this looks like the bedroom Hallway, its empty.",
   "This is the second bedrooms closet, funny looking sock on the ground...",
   "This is the bedrooms closet, their class notes are on the ground...",
   "You're in the storage hallway, not much storage.",
   "You're in the Hallway, theres a vase with ashes on the table."

]

NEWPAGE = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
#new page


def opening():                                  #def func
    print(NEWPAGE)                              #print new page
    print("\t\tGET BACK\n\n\t\tBy Jacob C\n\n") #print titile
    time.sleep(3)                               #sleep
    print(NEWPAGE)                                                                                      #print new page
    print("You finally tracked down the kid who was cyber bullying you, time to get some get back.")    #print backstory
    print("\nOBJECTIVE: LOOT, STEAL, TROLL")                                                            #print goal
    time.sleep(5)                                                                                       #sleep
    print(NEWPAGE)                                                                                      #print new page

    if str(input("ENTER 'H' FOR HELP MENU OTHERWISE ENTER ANY BUTTON TO CONTINUE ")).upper() == "H":    #print help
        print(NEWPAGE)                                                                                  #print new page
        print("WAYS YOU CAN GET BACK:")             #print msg
        print("\n\t1. TAKE BELONGINGS.")
        print("\t2. MOVE AROUND OBJECTS")
        print("\t3. LEAVE FAT DOOKIES")
        input("\nPRESS ANY BUTTON TOO CONTINUE")

    return

opening()

collected_items = []    #set var
dookies_taken = 0       #set var

fs_index = 2            #set var
se_index = 2            #set var
name_number_index = 2   #set var
while True:                                             #while true
    print("\n\n")                                       #print new line
    print(DESCRIPTIONS[name_number_index])              #print location
    if len(collected_items) == 6:                       #if user has all items
        print("OBJECTIVE: GET TO GARAGE AND LEAVE.")    #print objective

    if "Grandpas' Ashes" not in collected_items and name_number_index == 20:                                    #if user doesn't already have item and is in correct room
        if str(input("Wait should we take that... (y/n) ")).upper() == "Y":                                     #let user take item
            print('It reads: "Granpas Ashes"',"It's ours now.")                                                 #print msg
            collected_items.append("Grandpas' Ashes")                                                           #append item into list
            DESCRIPTIONS[name_number_index] = "You're in the Hallway, theres nothing on the table... anymore."  #update area msg
 
    elif "Family Photo" not in collected_items and name_number_index == 15:                                                             #if user doesn't already have item and is in correct room
        if str(input("Do you want to take it? (y/n) ")).upper() == "Y":                                                                 #let user take item
            print("There gonna miss this!")                                                                                             #print msg
            collected_items.append("Family Photo")                                                                                      #append item into list
            DESCRIPTIONS[name_number_index] = "You're in the Master Bedroom Hallway, these walls are bland"                             #update area msg

    elif "Cutlery" not in collected_items and name_number_index == 5:                                                                   #if user doesn't already have item and is in correct room
        if str(input("If we take these they'll have to eat with their hands. \nDo you want to take it? (y/n) ")).upper() == "Y":        #let user take item
            print("You are now the proud owner of 6 sets of cutlery!")                                                                  #print msg
            collected_items.append("Cutlery")                                                                                           #append item into list
            DESCRIPTIONS[name_number_index] = "You're in the Kitchen, they use paper plates?"                                           #update area msg

    elif "Walmart Shoes" not in collected_items and name_number_index == 6:                                     #if user doesn't already have item and is in correct room
        if str(input("We need some new shoes \nDo these look good enough for you? (y/n) ")).upper() == "Y":     #let user take item
            print("Great, let's grab them all while we're at it.")                                              #print msg
            collected_items.append("Walmart Shoes")                                                             #append item into list
            DESCRIPTIONS[name_number_index] = "You're in the Outer Foyer, it smells weird."                     #update area msg

    elif name_number_index == 14:                                                                               #if user is in right room
        if str(input("That bucket is a good spot to lay one out... (y/n)")).upper() == "Y":                     #let user dookie
            print("Sick, that'll teach em.")                                                                    #print msg
            dookies_taken += 1                                                                                  #update dookie counter

            if name_number_index == 14 and len(collected_items) == 6 and str(input("Are you ready to leave? (y/n)")).upper() == "Y":    #if uer meets requirments
                print("\n\nLeaving House...")                                                                                           #leave house
                break                                                                                                                   #break

        elif name_number_index == 14 and len(collected_items) == 6 and str(input("Are you ready to leave? (y/n)")).upper() == "Y":      #if user meets requirments
            print("\n\nLeaving House...")                                                                                               #leave house
            break                                                                                                                       #break

    elif "Envelopes" not in collected_items and name_number_index == 9:                                         #if user doesn't already have item and is in correct room
        if str(input("Let's take their mail... (y/n) ")).upper() == "Y":                                        #let user take item
            print("These look like bills and government support money. It's ours.")                             #print msg
            collected_items.append("Envelopes")                                                                 #append item into list
            DESCRIPTIONS[name_number_index] = "This looks like the Living room, another cardbord box table."    #update area msg

        if str(input("Why don't we leave steamer while we're here? (y/n)")).upper() == "Y":                     #let user dookie
            print("Jeez, that a nasty one.")                                                                    #print msg
            dookies_taken += 1                                                                                  #update dookies taken

    elif "Costco Samples" not in collected_items and name_number_index == 0:                                    #if user doesn't already have item and is in correct room
        if str(input("Do you want to take them? (y/n)")).upper() == "Y":                                        #let user take item
            print("Alright")                                                                                    #print msg
            collected_items.append("Costco Samples")                                                            #append item into list
            DESCRIPTIONS[name_number_index] = "This looks like a pantry room, there isn't any food here..."     #update area msg

    answer = str(input(f"\nYOU CAN GO NORTH, WEST, SOUTH, EAST: "))     #print options

    if answer.upper() == "INVENTORY":                                   #if user asks for inventory
        print("\nYOU HVAE COLLECTED: \n")                               #print msg
        for item in collected_items:                                    #print all items
            print(item)                                                 #print all items

    elif answer.upper() not in DIRECTIONS[fs_index]:                    #if user picks unsupported or invalid direction
        print("THERE IS NOTHING THERE...")                              #print msg
    
    else:                                                               #else
        se_index = DIRECTIONS[fs_index].index(answer.upper())           #set the second index to the index of the direction
        name_number_index = ADJACENCY_LIST[fs_index][se_index]          #set name index to the number in ad lis with the first index and second index
        fs_index = NAMES.index(NAMES[name_number_index])                #chanfe first index to the index of the name of area
      
    for event in pygame.event.get():            #Check for events
        if event.type == pygame.QUIT:           #Check if users x's out
            pygame.quit()                       #Quit pygame   
            sys.exit() 

    pygame.display.flip()           #Update screen

print("WELL DONE")                                  #print msg
print("\nYOU TOOK:")                                #print msg
for item in collected_items:                        #iterate through collected items
    print(item)                                     #print msg
print("\nYOU LEFT", dookies_taken, " DOOKIES.")     #print msg
    


