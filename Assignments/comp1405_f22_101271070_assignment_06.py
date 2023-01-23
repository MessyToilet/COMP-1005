'''
Date:           11/5/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Board Game
'''

import pygame           #import pygame
import random           #import random
import sys              #import sys
import time             #import time

pygame.init()                                       #init pygame

windowSize = (600, 800)                             #Choose window size
window = pygame.display.set_mode(windowSize)        #Set up display and call it window
window.fill("purple")                               #Set up window color 
clock = pygame.time.Clock()                         #init pygame clock

def snakes_ladders():                                       #def func
    snake_location = []                                     #create lis
    ladder_location = []                                    #create lis
    both = []                                               #create joint lis to pass
    for i in range(2):                                      #repeat twice
        snake_location.append(random.randint(1, 144))       #append a location

        ladder_location.append(random.randint(1, 144))      #append a location
    both.append(snake_location)                             #append snake locations
    both.append(ladder_location)                            #append ladder locations

    return(both)                                            #return the lis

    #Func creates two lists and creates two random points

def boardSetUp(locations):                  #create func

    tileColors = ["Red", "Blue"]            #set tile colors
    x   = 0                                 #set x
    y   = 550                               #set y
    z   = 0                                 #set z
    direction = 1                           #set direction
    tile_count = 0                          #set tile count
    snakes_ladder_locations = [[],[]]       #further develop the snakeladder list for coords for snakes and ladders
    for i in range(12):                     #repeat 12 times
        for k in range(12):                 #repeat 12 times
            tile_count += 1                 #increase tile count

            if tile_count in locations[0]:                                          #if tile count is one of the random numbers (re use random numbers as tile count spot)
                pygame.draw.rect(window, "green", pygame.Rect(x, y, 50, 50))        #draw a rect
                #pygame.draw.circle(window, (10, 10, 10), ((x + 25), (y + 25)), 1)   #draw circle for debugging
                snakes_ladder_locations[0].append(x + 25)                           #append x location
                snakes_ladder_locations[0].append(y + 25)                           #append y location
            elif tile_count in locations[1]:                                        #if tile count is a ladder
                snakes_ladder_locations[1].append(x + 25)                           #append x location
                snakes_ladder_locations[1].append(y + 25)                           #append y location
                pygame.draw.rect(window, "yellow", pygame.Rect(x, y, 50, 50))       #draw rect
                #pygame.draw.circle(window, (10, 10, 10), ((x + 25), (y + 25)), 1)   #draw cirlce for debug

            else:                                                                               #else
                pygame.draw.rect(window, tileColors[k % 2 - z], pygame.Rect(x, y, 50, 50))      #draw rect, filter through colors using mod, subtrack one when going backwards so mod is irellevent
                #pygame.draw.circle(window, (10, 10, 10), ((x + 25), (y + 25)), 1)               #draw cirlce for debuging

            font = pygame.font.SysFont( "timesnewroman", 20)        #create font                                    
            font = font.render(str(tile_count), True, 20)           #create font
            window.blit(font, (x, y))                               #blit font img
            x   += 50 * direction                                   #increase x by 50, or decrease by 50
        y   -= 50                                                   #subtract 50 from y
        if direction == 1:                                          #if direaction is forward (1)
            x = 550                                                 #set x to 550
            z = 1                                                   #make mod irrelvent
        else:                                                       #else
            x = 0                                                   #set x to 0
            z = 0                                                   #make mod relevent
        direction = direction * -1                                      #multiply direction by negative 1 to flip through forwards or backwards
        tileColors[0], tileColors[1] = tileColors[1], tileColors[0]     #revese the tile colors (may not need this now?)
    return(snakes_ladder_locations)                                     #return the lis                       

def draw_square(dx, dy):                                                #create func
    pygame.draw.rect(window, "white", pygame.Rect(dx, dy, 100, 100))    #draw a rect

#(150, 600) (350, 600)                                                  #colors

def draw_one(dx, dy):                                                   #draw a single dot (middle)
    pygame.draw.circle(window, "black", (dx + 50, dy + 50), 7)          #drwa dot

def draw_two(dx, dy):                                                   #create func
    pygame.draw.circle(window, "black", (dx + 25, dy + 75), 7)          #draw dot
    pygame.draw.circle(window, "black", (dx + 75, dy + 25), 7)          #draw dot (diagonally)

def draw_three(dx, dy):     #create func                                     
    draw_one(dx, dy)        #call draw one
    draw_two(dx, dy)        #call draw two

def draw_four(dx, dy):                                              #create func
    draw_two(dx, dy)                                                #call draw two
    pygame.draw.circle(window, "black", (dx + 25, dy + 25), 7)      #draw dot
    pygame.draw.circle(window, "black", (dx + 75, dy + 75), 7)      #draw dot

def draw_five(dx, dy):      #create func
    draw_four(dx, dy)       #call draw four
    draw_one(dx, dy)        #call draw one

def draw_six(dx, dy):       #create func
    draw_four(dx, dy)                                               #call draw four
    pygame.draw.circle(window, "black", (dx + 25, dy + 50), 7)      #draw dot
    pygame.draw.circle(window, "black", (dx + 75, dy + 50), 7)      #draw dot


def roll_dice():                                        #def func
    pos = [150, 650, 350, 650]                          #list postions of dice
    moves = 0                                           #declare moves/ sum
    for i in range(0,4,2):                              #repeat twice, but do 0, 4, 2 to skip ele in lis
        
        dice_roll = random.randint(1, 6)                #roll dice is random val, 1-6

        draw_square(    pos[i],    pos[int(i + 1)])     #draw square

        if dice_roll == 1:                              #if dice roll 1 
            draw_one(   pos[i],    pos[int(i + 1)])     #draw one

        elif dice_roll == 2:                            #if dice roll 2
            draw_two(   pos[i],    pos[int(i + 1)])     #draw two

        elif dice_roll == 3:                            #if dice roll 3
            draw_three( pos[i],    pos[int(i + 1)])     #draw three

        elif dice_roll == 4:                            #if dice roll 4
            draw_four(  pos[i],    pos[int(i + 1)])     #draw four

        elif dice_roll == 5:                            #if dice roll 5
            draw_five(  pos[i],    pos[int(i + 1)])     #draw 5

        elif dice_roll == 6:                            #if dice roll 6
            draw_six(   pos[i],    pos[int(i + 1)])     #draw 6
        #print("\n", dice_roll)#debug                     
        moves += dice_roll                              #sum dice rolls
    #print(moves)#debug
    return(moves)                                       #return moves


class player:                       #create class

    def __init__(self, color):      #create init
        self.x = 25                 #set init x val
        self.y = 575                #set ini y val
        self.color = color          #set init color
        self.forward = 1            #set init forward 1 (true)

    def draw(self):                                                     #create method
        pygame.draw.circle(window, self.color, (self.x, self.y), 20)    #draw player
    
    def move(self):                             #create method
        steps = roll_dice()                     #set steps to roll dice
        #print(steps)#debug
        for i in range(steps):                  #repeat for every step
            if self.x == 575 and self.y == 25:  #if player reached the end              
                print("end reached")            #tell user
                return True                     #return 

            #print(i)#debug        
            self.x += 50 * self.forward         #increase x by 50 or decrease by 50 (depending on direction/ "forward")
            #print("moving")#debug         
            locate = boardSetUp(locations)      #set locate as snake, ladder locations
            player1.draw()                      #draw characters
            player2.draw()                      #draw characters
            #print(locate)#debug
            if self.x > 575 or self.x < 20:     #if reaches the end of either side of the board
                self.y -= 50                    #deacrease y by 50
                if self.x > 575:                #if x was to big
                    self.x -= 50                #decrease x by 50, (off set so it doesn't go off screen)
                else:                           #else
                    self.x += 50                #increase by 50 (not sure why it needs to be ofset but it does)
                self.forward = self.forward * -1#change forward (monotonic sequence)
                   
            snakex1 = locate[0][0]      #declare var
            snakey1 = locate[0][1]      #declare var
            snakex2 = locate[0][2]      #declare var
            snakey2 = locate[0][3]      #declare var

            ladderx1 = locate[1][0]     #declare var
            laddery1 = locate[1][1]     #declare var
            ladderx2 = locate[1][2]     #declare var
            laddery2 = locate[1][3]     #declare var    

            if snakey1 > snakey2:#closer    snake1 is closer
                snake_tail_x = snakex1     #declare var
                snake_tail_y = snakey1     #declare var
                snake_head_x = snakex2     #declare var
                snake_head_y = snakey2     #declare var

            elif snakey1 == snakey2 and self.forward == 1 and snakex1 < snakex2:    #snake one and two are on the same row but snake one is closer  because of direction left to right
                snake_tail_x = snakex1     #declare var
                snake_tail_y = snakey1     #declare var
                snake_head_x = snakex2     #declare var
                snake_head_y = snakey2     #declare var

            elif snakey1 == snakey2 and self.forward == -1 and snakex1 > snakex2:   #snake one and two are on the same row but snake one is closer beacuse of direaction right to left
                snake_tail_x = snakex1     #declare var
                snake_tail_y = snakey1     #declare var
                snake_head_x = snakex2     #declare var
                snake_head_y = snakey2     #declare var

            elif snakey2 > snakey1:        #snake 2 is closer
                snake_tail_x = snakex2     #declare var
                snake_tail_y = snakey2     #declare var
                snake_head_x = snakex1     #declare var
                snake_head_y = snakey1     #declare var

            elif snakey1 == snakey2 and self.forward == 1 and snakex2 < snakex1:    #snake 2 and 1 are on the same row but snake two is closer because of direction (same as previous)
                snake_tail_x = snakex2     #declare var
                snake_tail_y = snakey2     #declare var
                snake_head_x = snakex1     #declare var
                snake_head_y = snakey1     #declare var

            elif snakey1 == snakey2 and self.forward == -1 and snakex2 > snakex1:   #snake 2 and 1 are on the same row but snake two is closer because of direcion
                snake_tail_x = snakex2     #declare var
                snake_tail_y = snakey2     #declare var
                snake_head_x = snakex1     #declare var
                snake_head_y = snakey1     #declare var

            if laddery1 > laddery2:          #ladder one is closer 
                ladder_tail_x = ladderx1     #declare var
                ladder_tail_y = laddery1     #declare var
                ladder_head_x = ladderx2     #declare var
                ladder_head_y = laddery2     #declare var

            elif laddery1 == laddery2 and self.forward == 1 and ladderx1 < ladderx2:    #ladder 1 and 2 are on the same row but ladder one is closer because of direction
                ladder_tail_x = ladderx1     #declare var
                ladder_tail_y = laddery1     #declare var
                ladder_head_x = ladderx2     #declare var
                ladder_head_y = laddery2     #declare var

            elif laddery1 == laddery2 and self.forward == -1 and ladderx1 > ladderx2:   #ladder 1 and 2 are on the same row but ladder one is closer becuase of direaction
                ladder_tail_x = ladderx1     #declare var
                ladder_tail_y = laddery1     #declare var
                ladder_head_x = ladderx2     #declare var
                ladder_head_y = laddery2     #declare var

            elif laddery2 > laddery1:        #ladder two is closer
                ladder_tail_x = ladderx2     #declare var
                ladder_tail_y = laddery2     #declare var
                ladder_head_x = ladderx1     #declare var
                ladder_head_y = laddery1     #declare var

            elif laddery1 == laddery2 and self.forward == 1 and ladderx2 < ladderx1:    #ladder 2 and 1 are on the same row but ladder 2 is closer beacuse of direaction
                ladder_tail_x = ladderx2     #declare var
                ladder_tail_y = laddery2     #declare var
                ladder_head_x = ladderx1     #declare var
                ladder_head_y = laddery1     #declare var

            elif laddery1 == laddery2 and self.forward == -1 and ladderx2 > ladderx1:   #ladder 2 and 1 are on the same row but ladder 2 is cloaser beacus of direaction
                ladder_tail_x = ladderx2     #declare var
                ladder_tail_y = laddery2     #declare var
                ladder_head_x = ladderx1     #declare var
                ladder_head_y = laddery1     #declare var

            if i + 1 == steps:                                              #if last step is reached
                if self.x == ladder_tail_x and self.y == ladder_tail_y:     #and if x is at a ladder
                    self.x = ladder_head_x                                  #set new point of x to top of ladder
                    self.y = ladder_head_y                                  #set new point of y to top of ladder
                    
                    self.forward = 1                            #reset forward            
                    if self.y in [i in range(25, 625, 100)]:    #if player is in creatan row
                        self.forward = -1                       #make them go apporpiate direation

                elif self.x == snake_head_x and self.y == snake_head_y: #if player lands on snake
                    self.x = snake_tail_x                               #make player go to snake tail x
                    self.y = snake_tail_y                               #make player go to snake tail y

                    self.forward = 1                            #reset forawrd again
                    if self.y in [i in range(25, 625, 100)]:    #cheack
                        self.forward = -1                       #change

            pygame.draw.circle(window, self.color, (self.x, self.y), 20)    #draw player
            pygame.display.flip()                                           #Update screen
            time.sleep(.5)                                                  #slow down


locations = snakes_ladders()    #call func 

player1 = player("Black")       #create character
player2 = player("white")       #create character
while True:                     #Main Loop
    boardSetUp(locations)       #draw board

    player1.draw()              #draw player
    player2.draw()              #draw player
    if player2.move() == True or player1.move() == True:    #if either player reached the end
        pygame.quit()                                       #quit
        sys.exit()                                          #fall back quit

    for event in pygame.event.get():            #Check for events
        if event.type == pygame.QUIT:           #Check if users x's out
            pygame.quit()                       #Quit pygame    
            sys.exit()                          #fall back quit

        #elif event.type == pygame.MOUSEBUTTONDOWN:      #debug
        #    x,y = pygame.mouse.get_pos()
        #    print(round(x/25) * 25, round(y/ 25) * 25)
          


    pygame.display.flip()           #Update screen
    clock.tick(60)                  #max tick rate 60

