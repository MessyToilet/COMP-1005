'''
Date:           11/19/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Matrix Addition
'''


def matrix_addition(matrix_a, matrix_b):                                        #def func
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):  #check if M1mn = M2mn
        return([])                                                              #return empty if not
    
    new_matrix = []                                                     #set new matrix
    for i in range(len(matrix_a)):                                      #repeat for every row
        new_matrix.append([])                                           #append an empty list to have same # of rows

    for i in range(len(matrix_a)):                                      #repeat for  ith location
        for k in range(len(matrix_a)):                                  #repeat for kth location
            new_matrix[i].append(matrix_a[i][k] + matrix_b[i][k])       #append M1ik + M2ik
    return(new_matrix)                                                  #return matrix


matrix1 =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2 = [ 
    [2, 3, 4],
    [5, 6, 7],
    [8, 9, 10]
]

print(matrix_addition(matrix1, matrix2))
print()
for row in matrix_addition(matrix1, matrix2):
    print(row)
