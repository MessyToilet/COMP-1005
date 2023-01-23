'''
Date:           9/23/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Grade Calculator
'''

'''                         #Debug
val1 = 100 * 10
val2 = 1 * 40
val3 = 100 * 30
val4 = 100 * 20

vall = val1/100 + val2/100 + val3/100 + val4/100 


print(vall)

lis = [[10], [10], [10]]

lis[0].append(15)

lis[1].append(13)

lis.append(5)

print(lis)
'''

answers = []                                                                #Initalize lis
ques = ["tutorial work?", "assignemnts?", "midterm/ quizes?", "final?"]     #Initalize lis

for i in range(4):                                                          #delcare loop
    userInput = input(f'\n What grade did you get for the {ques[i]}: ')     #get input
    try:                                                                    #test input
        int(userInput)                                                              
    except:                                                                 #if input fails test...
        print("Input given not an integer, quiting program...")
        quit()
    answers.append(userInput)                                               #append input to lis

weighedAnswers = [[10 ], [40 ], [30 ], [20 ]]                               #declare lis
numAvg = 0                                                                  #declare var

for i in range(len(answers)):                                                                   #declare loop
    weighedAnswers[i].append( int((int(answers[i]) * int(weighedAnswers[i][0])) // 100))        #appened calculated grade
    numAvg += int(weighedAnswers[i][1])                                                         #add to var
    
#print(numAvg)      #Debug
#declare lis
gradingScheme = [["A+", 90], ["A", 85], ["A-", 80], ["B+", 77], ["B", 73], ["B-",70], ["C+", 67], ["C", 63], ["C-", 60], ["D+", 57], ["D", 53], ["D-", 50], ["F", 0]]

for i in range(len(gradingScheme)):                     #declare loop
    if numAvg >= gradingScheme[i][1]:                   #see if grade is higher than grading scheme
        print("Your grade is", gradingScheme[i][0])     #if so print grade
        break                                           #break out of loop