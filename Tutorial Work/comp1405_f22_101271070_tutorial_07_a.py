'''
Date:           11/19/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Matrix Validity Test
'''

"""
matrix=[ 
    [1,2],
    [1.5,1.6]
    
]
 """
def is_matrix(matrix):                                          #def func
    try:                                                        #Try, because if lis is not given we can iterate over the input
        for row in matrix:                                      #Check for each row...    
            if not isinstance(row, list):                       #is the ele a row?
                return(False)                                   #if yes return false
            
            if len(row) != len(matrix):                         #if the length of the row (colums) not equal to length of the matrix(rows)
                return(False)                                   #return False

            for item in row:                                    #iterate through items in row 
                if isinstance(item, str):                       #if item is a string
                    return(False)                               #return False
    except:                                                     #if we can iterate or continue to iterate
        return(False)                                           #return false

    return(True)                                                #if input passes test return True

#print(is_matrix(matrix))