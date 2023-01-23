'''
Date:           10/19/2022
Name:           Jacob Chiu
Student Number: 101271070
Course:         COMP 1005 B
Assignmnent:    Number Pyramid
'''

while True:
    num = [input('Provide int 1-9: '), 1]
    try:
        if int(num[0]) < 10 and int(num[0]) > 0:
            break
    except:
        pass

while True:
    print(str(num[1]) * int(num[1]))
    if num[1] == int(num[0]):
        break 
    num[1] += 1

# while True:
#     nums = [input("Provide an integer 1-9: "), 1]
#     if int(nums[0]) in [x for x in range(1, 10)]:
#         break

# while True:
#     print(str(nums[1]) * int(nums[1]))
#     if nums[1] == int(nums[0]) : 
#         break
#     nums[1] += 1

