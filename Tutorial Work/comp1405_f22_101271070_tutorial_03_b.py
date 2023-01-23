'''
Date:           9/23/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Oregon Trail Copy
'''

game = {"players": {1: ["Banker", 1600], 2: ["Carpenter", 800], 3: ["Farmer", 400]}, "store": {1: ["Oxen", 10, "per ox", 0.00, "How many oxen"], 2: ["Food", .20, "per pound", 0.00, "How many pounds of food"], 3: ["Clothing", 10, "for one set", 0.00, "How many sets of clothes"], 4: ["Ammunition", 2, "per box of 20 bullets", 0.00, "How many boxes"], 5: {1: ["Wagon wheel", 10, 0.00], 2: ["Wagon axle", 10, 0.00], 3: ["Wagon tongue", 10, 0.00]}}}
newPage = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
gameOn = True
passing = False
bill = 0.00
buyWhat = 0
buyMenu = 0

gameLoadScreen = f"------------------------------------\n\tChoose a profesion \n------------------------------------ \nYou May: \n1. Be a {game['players'][1][0]} \n2. Be a {game['players'][2][0]} \n3. Be a {game['players'][3][0]}" 

print(gameLoadScreen)
professionKey = int(input("What is your choice? "))

while professionKey not in [1, 2, 3]:                     
    professionKey = int(input("Pick a number from the choices "))

gameShopScreen = f"------------------------------------\n\tWatt's General Store \n------------------------------------ \n1. {game['store'][1][0]}\t\t\t${game['store'][1][3]} \n2. {game['store'][2][0]}\t\t\t${game['store'][2][3]} \n3. {game['store'][3][0]}\t\t${game['store'][3][3]} \n4. {game['store'][4][0]}\t\t${game['store'][4][3]} \n5. Spare Parts\t\t${game['store'][5][1][2] + game['store'][5][2][2] + game['store'][5][3][2]} \n------------------------------------ \n\tTotal Bill ${bill} \n\nAmount you have: ${game['players'][int(professionKey)][1]}"

print(newPage + gameShopScreen)

while gameOn:
    while buyWhat not in [1, 2, 3, 4, 5]:
        buyWhat = int(input("\nWhich item would you like to buy? "))                                #changed to int input so i dont have to add int()
        if buyWhat == 0: 
            print(f'\nLeaving Store...')
            gameOn = False  
            passing = True  
            break
        if buyWhat in [1, 2, 3, 4]:
            buyMenu = (f'{game["store"][int(buyWhat)][0]} cost ${game["store"][int(buyWhat)][1]} {game["store"][int(buyWhat)][2]}')
        elif buyWhat == 5:
            buyMenu1 = (f'{game["store"][int(buyWhat)][1][0]} cost ${game["store"][buyWhat][1][1]} each')
            buyMenu2 = (f'{game["store"][buyWhat][2][0]} cost ${game["store"][buyWhat][2][1]} each')
            buyMenu3 = (f'{game["store"][buyWhat][3][0]} cost ${game["store"][buyWhat][3][1]} each')
        else:
            print("\nPick a number from the choices")
    if passing == False:
        if buyWhat == 5:
            print(f"{newPage}------------------------------------\n\tWatt's General Store \n------------------------------------ \n\n{buyMenu1} \n{buyMenu2} \n{buyMenu3}")
            for i in range(1, 4):
                game["store"][buyWhat][i][2] += round(float(float(game["store"][buyWhat][i][1]) * int(input(f'\n\tTotal Bill ${bill} \n\nHow many {game["store"][buyWhat][i][0]}s would you like to buy? '))), 2)
                print(f"{newPage}------------------------------------\n\tWatt's General Store \n------------------------------------ \n\n{buyMenu1} \n{buyMenu2} \n{buyMenu3}")
                bill += round(game["store"][buyWhat][i][2], 2)

        else:       #buying oxen, food, clothes, or bullets
            print(f"{newPage}------------------------------------\n\tWatt's General Store \n------------------------------------ \n\n{buyMenu} \n\n\tTotal Bill ${round(bill)} \n\nHow many {game['store'][int(buyWhat)][4]} would you like to buy? ", end = '')
            game["store"][int(buyWhat)][3] += round(float(float(game["store"][int(buyWhat)][1]) * int(input())), 2)
            bill += round(game["store"][int(buyWhat)][3], 2)

        print(f"{newPage}------------------------------------\n\tWatt's General Store \n------------------------------------ \n1. {game['store'][1][0]}\t\t\t${round(game['store'][1][3], 2)} \n2. {game['store'][2][0]}\t\t\t${round(game['store'][2][3], 2)} \n3. {game['store'][3][0]}\t\t${round(game['store'][3][3], 2)} \n4. {game['store'][4][0]}\t\t${round(game['store'][4][3], 2)} \n5. Spare Parts\t\t${round(game['store'][5][1][2] + game['store'][5][2][2] + game['store'][5][3][2], 2)} \n------------------------------------ \n\tTotal Bill ${round(bill, 2)} \n\nAmount you have: ${round(game['players'][int(professionKey)][1], 2)}")
        buyWhat = 100
        print('\nEnter "0" when you want to leave the store')
    else:
        pass


print(f'you bought:')

for i in range(1, 8):
    if i < 5 and round((float(game["store"][i][3]) / float(game["store"][i][1])), 2) == 1.00:
       # if round((float(game["store"][i][3]) / float(game["store"][i][1])), 2) == 1.00:
        if i == 1:
            print(f'\n1 oxen for ${game["store"][i][3]}')
        if i == 2:
            print(f'\n1 pound of food for ${game["store"][i][3]}')
        if i == 3:
            print(f'\n1 set of clothes for ${game["store"][i][3]}')
        if i == 4:
            print(f'\n1 box of bullets for ${game["store"][i][3]}')
    elif i >= 5 and round((float(game["store"][5][i % 4][2]) / float(game["store"][5][i % 4][1])), 2) == 1.00:      #take mod4 to stay within the lim of the dict
       # if round((float(game["store"][5][i][3]) / float(game["store"][5][i][1])), 2) == 1.00:
        if i == 5:
            print(f'\n1 wagon wheel for ${game["store"][5][1][2]}')
        if i == 6:
            print(f'\n1 wagon axle for ${game["store"][5][2][2]}')
        if i == 7:
            print(f'\n1 wagon tongue for ${game["store"][5][3][2]}')
    else:
        if i == 1:
            print(f'\n{round(game["store"][i][3] / game["store"][i][1], 1)} oxen for ${game["store"][i][3]}')
        if i == 2:
            print(f'\n{round(game["store"][i][3] / game["store"][i][1], 1)} pounds of food for ${game["store"][i][3]}')
        if i == 3:
            print(f'\n{round(game["store"][i][3] / game["store"][i][1], 1)} sets of clothes for ${game["store"][i][3]}')
        if i == 4:
            print(f'\n{round(game["store"][i][3] / game["store"][i][1], 1)} boxes of bullets for ${game["store"][i][3]}')
        if i == 5:
            print(f'\n{round(game["store"][5][1][2] / game["store"][5][1][1], 1)} wagon wheels for ${game["store"][5][1][2]}')
        if i == 6:
            print(f'\n{round(game["store"][5][2][2] / game["store"][5][2][1], 1)} wagon axles for ${game["store"][5][2][2]}')
        if i == 7:
            print(f'\n{round(game["store"][5][3][2] / game["store"][5][3][1], 1)} wagon tongue for ${game["store"][5][3][2]}')

print(f'\nYour total bill is ${bill}', end = ", ")
if bill > game["players"][professionKey][1]:
    print(f"you dont have enough money to afford these items... \n")
else:
    print(f"you are left with ${round(game['players'][professionKey][1] - bill, 2)} \n")

'''Pseudo Code

Define game Dict, this will be used to call to specific parts and details of the game/ calculator. Important values will be stored here.
Define new page as \n repeating, to give the ilusion of a new page
define conditional vars game on and passing, these will be used to end/ keep main program going
define vars

define load screen layout/ ascii art
print load screen
ask what profession user wants to be, this will be the key for the dict

if user inputs number that is not a key for dict ask user to try again

define game screen/ ascii art

print new page and game screen

while game on is true   
    and while user didn't specify what they want to buy
        ask user what they want to buy

        here we also include the eixting arguments, so user doesn't go throught this page again, and we can utilise the sane user input (happens if user picks 0, only prompted after)

        if the user picked 1, 2, 3, or 4
            define the buy menu for the item they picked, use the user input as the key for the specific items details like name and price

        elif user picked 5
            define multiple buy menus for option 5, because option 5 is a dict in a dict (I could've used the mod4 here to reduce the amount of menus needed, but then i would have to resturcture my progam)

        else (user didn't pick given number)
            ask again

        check if passing is false
            if user input was 5
                print the buy menus for option 5
                cylce through the things the user can buy in option 5
            
            else (user input was 1, 2, 3, 4)
                go to the buy screen for the option they picked, use unique phrases from the dict
            
            print a new page and the store page
            set buyWhat (user input) to a random value to break out of loop, this causes the program to ask what user wants to buy again
            also tell user how to leave the store

            if user chooses to leave the store switch passing to True so it passes the second part, set gameOn to false to end main loop and break out of loop

print you bought

user for loop to cycle through range to aviod coding conditions for every item

in for loop check if item divides to one, if so only one item was bought, print message and other details

    else
        print how many/much of something the user bought and other details

calculate total bill and see if the user can afford it with the character they chose

if not, let user know

if they can tell user how much money they have left.
'''   

#Learning Dictionaries
#test ={1 : "hi", 2 : 10, "shop" : {1 : "hey", 2 : 5}}