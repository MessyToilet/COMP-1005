'''
Date:           11/12/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Homemade Dict
'''

def remove_punc(string):                                    #def func
    punc = [",", ".", "!", "?",'-', '_', "'",'"',";",":"]   #delcare what counts as punctuation
    new_str = ""                                            #set new string var
    for i in range(len(string)):                            #iterate through string
        if string[i] in punc:                               #if the character in string is in pung
            pass                                            #do nothing
        else:                                               #otherwise
            new_str = new_str + string[i]                   #build new string with character in string
    return(new_str)                                         #return the new stirng

def make_upper(string):                                     #def func
    new_str = ""                                            #set new string var
    for letr in string:                                     #iterate through string
        if letr == " ":                                     #if the character is a space
            new_str = new_str + " "                         #add a space to the new string
        elif ord(letr) > 90:                                #if the characters ord is greater than 90 (lower case)
            new_letr = int(ord(letr) - 32)                  #set new letter to be the upper case of the letter
            new_str = new_str + chr(new_letr)               #build new string with the upercase letter
        else:                                               #else (letter is alread upper case)
            new_str = new_str + chr(new_letr)               #build new string
    return(new_str)                                         #return new string

def acronym(string):                                        #def func
    words = [                                               #Declare supported acronyms     
        ["LAUGHING", "OUT", "LOUD", "LOL"],                 #   - Very important that acros are same length
        ["OH", "MY", "GOD", "OMG"],                         
        ["BY", "THE", "WAY", "BTW"],
        ["AWAY", "FROM", "KEYBOARD", "AFK"],   
    ]

    new_str = string                                        #set new string to be string parameter
    str_lis = []                                            #set empty list to hold each word        
    index_holder = 0                                        #set index holder to 0
    new_str = new_str + " "                                 #add a space to the end so the program can grab the last ele - since spaces trigger the program
    for i in range(len(new_str)):                           #repeat for each character in str
        if new_str[i] == " ":                               #if loop reaches a space
            str_lis.append(new_str[index_holder : i])       #append a splice of the string from the index holder up until the space
            index_holder = i + 1                            #set index holder to be the next index of the space
    
    updated_str = ""                                                                                    #set updated string
    for acro in words:                                                                                  #iterate over words
        for i in range(len(str_lis)):                                                                   #repeat for each word in str lis
            try:                                                                                        #check:
                str_lis[i + 2]                                                                          #if it is possible to have two words after current word (insures program doesn't run if a b c by) is given
            except:                                                                                     #if it can't
                break                                                                                   #break

            if str_lis[i] == acro[0] and str_lis[i + 1] == acro[1] and str_lis[i + 2] == acro[2]:       #if the first word matches with the first word in words, and so does the second and thrid
                updated_str = ""                                                                        #reset updated string (prevents repition)
                if len(updated_str) == 0:                                                               #if updated string is empty
                    updated_str = str_lis[0]                                                            #set the first word to the first word in str lis (str lis used to store previous string)
                    for k in range(1, i):                                                               #repeat form second word until the first acronym word is reached  
                        updated_str = updated_str + " " + str_lis[k]                                    #build string

                    updated_str = updated_str + " " + acro[3]                                           #build string with acronym word

                    for k in range(i + 3, len(str_lis)):                                                #build rest of the string
                        updated_str = updated_str + " " + str_lis[k]                                    #build string               - REMOVE THIS PART? JUST BUILD FULL ACRONYM THEN ADD REST

                else:                                                                                   #if string isn't empty
                    for k in range(0, i):                                                               #start from the first word to acronym word
                        updated_str = updated_str + " " + str_lis[k]                                    #build string

                    updated_str = updated_str + " " + acro[3]                                           #build string with acronym  - REMOVE THIS PAR? IF FULL ACRO IS BUILT BEFORE

                    for k in range(i + 3, len(str_lis)):                                                #build rest of string three words after, ONLY USEFULL IF WE BUILD FULL ACRO?
                        updated_str = updated_str + " " + str_lis[k]                                    #build string
        
        str_lis = []                                                #reset string list
        index_holder = 0                                            #set index holder to 0
        updated_str = updated_str + " "                             #add a space to updated string
        for i in range(len(updated_str)):                           #repeat for each character
            if updated_str[i] == " ":                               #if a space is reached
                str_lis.append(updated_str[index_holder : i])       #append the word
                index_holder = i + 1                                #increase index holder

        updated_str = ""                                            #reset updated string
        for word in str_lis:                                        #Iterate over str lis
            updated_str = updated_str + word + " "                  #set updated str to words in str lis - important otherwise loop won't engage, truely resset after in loop

    if updated_str == "    ":                                       #if updated str is four spaces, i.e nothing was done so program added spaces
        return(string)                                              #return input string
    
    return(updated_str)                                             #return updated string

def homoglyph(string):          #Def func
    letter_bank = [             #Declare translation key
        ["A", "4"],
        ["B", "I3"],
        ["C", "<"],
        ["D", "[)"],
        ["E", "3"],
        ["F", "/="],
        ["G", "6"],
        ["H", "#"],
        ["I", "!"],
        ["J", "_]"],
        ["K", "|<"],
        ["L", "|_"],
        ["M", "11"],
        ["N", "/V"],
        ["O", "0"],
        ["P", "|7"],
        ["Q", "(_,)"],
        ["R", "I2"],
        ["S", "5"],
        ["T", "7"],
        ["U", "LI"],
        ["V", "|/"],
        ["W", "VV"],
        ["X", "><"],
        ["Y", "`/"],
        ["Z", "%"]
    ]
    new_str = ""                                #set new string to nothing
    for i in range(len(string)):                #repeat for each character in string
        for letter in letter_bank:              #iterate over letter bank
            if string[i] == letter[0]:          #if character is the same a the character in the letter bank
                new_str = new_str + letter[1]   #build string with the translation - this is true for all characters since we removed punc and user shouldn't put numbers
            if string[i] == " ":                #if the character is a space
                new_str = new_str + " "         #build string
                break                           #break beacuse it will continue to check and add spaces even though we found the character

    return(new_str)                             #return new string

def main(string):                                               #def func
    print(remove_punc(string))                                  #print the output of func with a func passed as prameter
    print(make_upper(remove_punc(string)))                      #print the output of func with a funcs passed as prameter
    print(acronym(make_upper(remove_punc(string))))             #print the output of func with a funcs passed as prameter
    print(homoglyph(acronym(make_upper(remove_punc(string)))))  #print the output of func with a funcs passed as prameter

main(str(input(f"Input string: ")))                             #call with user input


