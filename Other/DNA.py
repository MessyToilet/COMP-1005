import random 
import itertools

name    = str(input(f'Hello, welcome to DNA game - a2.py. \n\nWhat is your name? '))
rules   = "\nIn this game you will: \n\n\t1. Find the complement of a DNA strand. \n\t2. Find the reversed DNA strand. \n\t3. Find the compressed DNA strand. \n\t4. Find the expanded DNA strand."
choices = "\n\n\t1. Complement (2 points) \n\t2. Reverse (2 points) \n\t3. Compress (3 points) \n\t4. Expand (3 points) \n\t5. Quit"
score   = 0
print(rules)

num     = input("\nPlease provide a natrual number for DNA length: ")
gameON    = True

def createDNA(num):
    dna = ""
    dnals = ["A", "C", "G", "T"]
    for i in range(int(num)):
        randNum2 = random.randint(0, 3)
        dna = dna + dnals[randNum2]
    return(dna)

def complementAns(complementHolder):
    dnaAns = ""
    for i in range(len(complementHolder)):
        if complementHolder[i] == "A":
            dnaAns = dnaAns + "T"
        if complementHolder[i] == "C":
            dnaAns = dnaAns + "G"
        if complementHolder[i] == "G":
            dnaAns = dnaAns + "C"
        if complementHolder[i] == "T":
            dnaAns = dnaAns + "A"
    return(dnaAns)

def reverseAns(complementHolder):
    return(complementHolder[::-1])

def compressedAns(complementHolder):
    dnaAns = ""
    for chr, count in itertools.groupby(complementHolder):
        g = list(count)
        if len(g) > 1:
            dnaAns = dnaAns + (str(len(list(g))) + chr)
        else:
            dnaAns = dnaAns + chr
    return(dnaAns)


while num.isnumeric() == False:
    try:
        num > 0
    except:
        num = input("\nPlease provide a natrual number: ")


while gameON:
    complementHolder = createDNA(num)
    print(f'\nThe DNA strand you are working with: {complementHolder}')

    print(choices)
    choice = str(input("\nPick a number: "))
    while choice not in ["1", "2", "3", "4", "5"]:
        choice = str(input("\nPick a number: "))

    if choice == "1":

        if input(f'\nWhat is the compliment to {complementHolder}? ').upper() ==  complementAns(complementHolder):
            print("\nCorrect!")
            score += 2
        else:
            print("\nIncorrect...")
            score -= 1

    if choice == "2":

        if input(f'\nWhat is the reverse of {complementHolder}? ').upper() == reverseAns(complementHolder):
            print("\nCorrect!")
            score += 2
        else:
            print("\nIncorrect...")
            score -= 1

    if choice == "3":
        if input(f'\nWhat is {complementHolder} compressed? ').upper() == compressedAns(complementHolder):
            print("\nCorrect!")
            score += 3
        else:
            print("\nIncorrect...")
            score -= 1

    if choice == "4":
        if input(f'\nWhat is the expanded version of {compressedAns(complementHolder)}? ').upper() == complementHolder:
            print("\nCorrect!")
            score += 3
        else:
            print("\nIncorrect...")
            score -= 1

    print("Score:", score)

    if choice == "5":
        if score >= 10:
            print(f'\nCongratulations {name}, your final score is {score}!')
        else:
            print(f"\nThanks for playing {name}, your final score is {score}!")
        gameON = False




    
    