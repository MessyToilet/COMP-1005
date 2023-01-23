'''
Date:           10/4/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Logical Operators
'''

import sys

a = sys.argv[1]         #define var
b = sys.argv[2]         #define var
c = sys.argv[3]         #define var
e = sys.argv[4]         #define var    
h = sys.argv[5]         #define var
i = sys.argv[6]         #define var
g = sys.argv[7]         #define var

#assignmet asks for 12 inputs, but my logic chart only has 7 unique inputs

result1 = (((not c) and ((a) or (((b) and (not e))))))      #determin result
result2 = (((g) and ((g) or ((not i) and (not h)))))        #determin result

# print(bool(result1))
# print(bool(result2))

print(f'<{bool(result1)},{bool(result2)}>')                 #print result