"""radius = input("What is the radius? ")      #Ask for radius
height = input("What is the height? ")      #Ask for height

volume = (float(radius) ** 2) * (3.14159 * float(height)) / 3       #Calculate vol

print(f"{volume:.4f}")      #print outcome

"""

"""
import pygame                               #Import pygame

windowSize = (750, 750)                 #Choose window size
windowColor = "White"                   #Choose bg color
windowCaption = "Quiz 1"          #choose caption text

window = pygame.display.set_mode(windowSize)            #Set up display and call it window
window.fill(windowColor)                                #Set up window color 
pygame.display.set_caption(windowCaption)               #Write caption text

star(i, j, r, g, g)         #Given func
umbrella(i, j, g, b)        #Given func

for i in range(1, 10, 4):               #create range, starting at 1, end at 9, count by 4
    for j in range(1, 12, 2):           #create range, starting at 1, end at 11, count by 2
        umnrella(i * 5, j + 1, 255, 0, 0)   #call star and pass parameters
        #print(i, j)
       
for i in range(4, 15, 2):               #create range, starting at 4, end at 14, count by 2
    for j in range(1, 8, 2):            #create range, starting at 1, end at 7, count be 2
        star(i, j, 0, 255, 0)       #call star func and pass parameters
        #print(i, j)

pygame.time.delay(5000)     #wait 5 seconds
"""

"""
count = 20          #define var
first = 37          #define var
while count > 0:    #define loop
    print(first)    #print
    first += 7      #add var
    count -= 1      #reduce var
"""
"""
#brocade, earthy, lindsay, delight, instable, bluefish

if input("Does your word have an 'o'? y/n ") in ["y", "Y"]:
    print("your word is brocade")

else:
    if input(f"does your word have an 'n'? y/n ") in ["y", "Y"]:
        print(f'your word is lindsay')

    else:
        if input(f"does your word have an 'f'? y/n ") in ["y", "Y"]:
            print(f'your word is bluefish')

        else:
            if input(f"does your word have an 'l'? y/n ") not in ["y", "Y"]:
                print(f"your word is earthy")

            else:
                if input(f"does your word have an 'd'? y/n ") in ["y", "Y"]:
                    print(f"your word is delight")

                else:
                    print(f"your word is instable")
"""


count = 20
first = 29
while True:
    print(first)
    first += 12
    if count < 1:
        break
