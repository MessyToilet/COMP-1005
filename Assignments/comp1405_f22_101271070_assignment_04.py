'''
Date:           10/16/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Movie Libary
'''
 
if input("Road movies or Christmas movies? (r/c) ") in ["c", "C"]:                          #Q1                                  #in christmas movies
    if input(f"Was your movie released between 1983 and 1994? (y/n) ") in ["y", "Y"]:       #Q2
        if input(f'Was your movie released between 1983 and 1985? (y/n) ') in ["y", "Y"]:   #Q3
            if input(f'was your movie released in 1983? (y/n) ') in ["y", "Y"]:print('Your movie is "A christmas Story", released in 1983.')   #Q4 check if input meets condition, if it does print
            else:    print(f'You movie is "Sanata Claus: The Movie", released in 1985.')                                                       #else print other statement
        else:                           
            if input("Was your movie released in 1988? (y/n) ") in ['y',"Y"]:print(f'Your movie is "Scrooged", released in 1988.') #Q4 check if input meets condition, if it does print
            else:    print(f'Your movie is "Jack Frost", released in 1998')                                                         #else print other statement
    else:
        if input(f'Was your movie released between 1999 and 2004? (y/n) ') in ["y", 'Y']:   #Q3                                  
            if input("Was your movie released in 2000? (y/n) ") in ["y", 'Y']:print(f'Your movie is "How the Grinch Stole Christmas", released in 2000.') #Q4 check if input meets condition, if it does print
            else:
                if input("Was your movie released in 2003? (y/n) ") in ["y", 'Y']:print('Your movie is "Bad Santa", released in 2003.')   #Q5 check if input meets condition, if it does print
                else:   print('Your movie is "Christmas with the Kranks", released in 2004.')#else print other statement
        else:
            if input("Was your movie released in 2005? (y/n) ") in ["y", 'Y']:print('Your movie is "Joyeux Noel", released in 2005.')        #Q4   check if input meets condition, if it does print  
            else:
                if input("Was your movie released in 2014? (y/n) ") in ["y", 'Y']:print('Your movies is "Get Santa", released in 2014.') #Q5 check if input meets condition, if it does print
                else:    print('Your movies is "A Christmas Horror Story", released in 2015.')#else print other statement
else:                                                                                           #in road movies
    if input(f'Was your movie released between 1937 and 1964 (y/n) ')  in ["y","Y"]:            #Q2
        if input(f'Was your movie released between 1937 and 1955 (y/n) ')  in ["y","Y"]:        #Q3
            if input("Was your movie released in 1936? (y/n) ") in ["y","Y"]:print('Your movies is "you only live once", released in 1937.') #Q4 check if input meets condition, if it does print
            else:
                if input("Was your movie released in 1939? (y/n) ") in ["y", "Y"]:print('Your movie is "Persons in hiding", released in 1939.')   #Q5 check if input meets condition, if it does print
                else:    print('Your movie is "They live by night", released in 1949.')      #else print other statement
        else:
            if input("Was your movie released between 1956 and 1973 ") in ["y", "Y"]:       #Q4
                if input("Was your movie released between 1956 and 1967? (y/n) ") in ["y", "Y"]:    #Q5
                    if input("Was your movie released in 1963? (y/n)? ") in ["y", "Y"]:print('Your movie is "The sadist", released in 1963.')  #Q6 check if input meets condition, if it does print
                    else:    print('Your movie is "Bonnie and Clyde", released in 1967.') #else print other statement
                else:
                    if input("Was your movie released in 1972? (y/n)? ") in ["y", "Y"]:print('Your movie is "The Get Away", released in 1972') #Q6 check if input meets condition, if it does print
                    else:    print('Your movie is "Badlands", released in 1973')#else print other statement
    else:
        if input(f'Was your movie released in 1990 (y/n) ') in ["y","Y"]:print('Your movie is "Wild at Heart", released in 1990.')   #Q3 check if input meets condition, if it does print
        else:    print('Your movie is "Thelma and Louise", 1991.')#else print other statement


"""
roadMovies = [

                    ["you only live once",              1937],
                    ["Persons in hiding",               1939],
                    ["They live by night",              1949],
                    ["The sadist",                      1963],
                    ["Bonnie and Clyde",                1967],
                    ["the get away",                    1972],
                    ["Badlands",                        1973],
                    ["Big Bad Mama",                    1974],
                    ["Wild at Heart",                   1990],
                    ["Thelma and Louise",               1991],

]
 
christmasMovies = [

                    ["A Christmas Story",               1983],
                    ["Santa Claus: The Movie",          1985],
                    ["Scrooged",                        1988],
                    ["Jack Frost",                      1998],
                    ["How the Grinch Stole Christmas",  2000],
                    ["Bad Santa",                       2003],
                    ["Christmas with the Kranks",       2004],
                    ["Joyeux Noel",                     2005],
                    ["Get Santa",                       2014],
                    ["A Christmas Horror Story",        2015],
                                         
]

"""
"""
roadmovielettercount    = []
roadmoviedatecount      = []
roaddateReleaseRange    = [1934, 1962, 2001, 1990, 2019]
roadletterRange         = []

chrismovielettercount   = []
chrismoviedatecount     = []
chrismovieReleaseRange  = [1983 , 1988, 1994, 2005, 2015]
chrismovieletterRange   = []

"""

"""#                        TRY GUESSING MOVIES USING LETTER FREQUENCY
def findFreq(lis):
    freq = {}
    for item in lis:
        if item in freq:
            freq[item] += 1

        else:
            freq[item] = 1

    for key, value in freq.items():
        print("% d : % d"%(key, value))


for i in range(len(roadMovies)):
    roadmoviecount = len([ele for ele in roadMovies[i][0] if ele.isalpha()])
    roaddate = roadMovies[i][1]
    roadmovielettercount.append(roadmoviecount)
    roadmoviedatecount.append(roaddate)
    #print(roadmoviecount)
    #print(date)


for i in range(len(christmasMovies)):
    chrismoviecount = len([ele for ele in christmasMovies[i][0] if ele.isalpha()])
    chrisdate = christmasMovies[i][1]
    chrismovielettercount.append(chrismoviecount)
    chrismoviedatecount.append(chrisdate)
    #print(chrismoviecount)

findFreq(chrismoviedatecount)
findFreq(chrismovielettercount)
findFreq(roadmoviedatecount)

findFreq(roadmovielettercount)
"""
#print(roadMovies)



#print(f"\n{min(dates)} is the oldest and {max(dates)} is the newest with {repeats} repeats")




#Determining movie algorithm
#Was the movie released in the range? 
#Does the movies name have this range amoung of letters? 
#7 questions, 3 realse date, 3 movie name lenght, one extra

