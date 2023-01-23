import random

def foo():
    for i in range(0, 21, 2):
        print(i)

def bar():
    less = 0
    equal = 0
    more = 0
    for i in range(100):
        int = random.randint(1, 6)
        if int == 4:
            equal += 1
        elif int > 4:
            more += 1
        else:
            less += 1

    return(less, more, equal)

def qux(bool1, bool2, int):
    var1 = bool1 
    var2 = bool2 
    var3 = int

    if var3 < 0:
        print((var1 and var2))
    else:
        print((var1 or var2))

def aap(bool1, char1, bool2, char2):

    var1 = bool1 
    var2 = char1
    var3 = bool2 
    var4 = char2
    lis = []
    if var1:
        lis.append(chr(var2))
        if var3:
            lis.append(chr(var4))
    return(lis)

"""
var_1 = 1
var_2 = 2
var_3 = 3
var_4 = 4

def foo(x):
    return 100 + x

def bar(var_2):
    var_2 += 100

def qux():
    global var_3
    global var_4
    var_3 += 100

def main():
    global var_1
    var_1 = foo(var_1)


bar(var_2)
qux
main()
 """   

def foo():
    return([x for x in range(0, 10_000) if x % 2 != 0])

def bar():
    lis = []
    for i in range(100):
        lis.append(chr(random.randint(65, 90)))
    return(lis)

def qux(lis):
    for i in range(20):
        lis.insert(random.randint(1, len(lis)), "?")
    return(lis)

def aap(lis):
    for i in range(random.randint(1, len(lis))):
        lis.append("!")
    return(lis)
#print(foo())
#print(bar())

def ham(lis):
    for ele in lis:
        try:
            lis.remove("A")
        except:
            break 
    return(lis)

def egg(lis):
    while "Z" in lis:
        lis.pop(0)

    return(lis)

def foo2():
    adMatrix = [
    #    0   1   2   3   4   5   6   7
        [0,  1,  0,  1,  0,  0,  1,  0], 
        [1,  0,  0,  0,  0,  1,  0,  1], 
        [0,  0,  0,  0,  0,  0,  0,  1], 
        [1,  0,  0,  0,  0,  0,  0,  0], 
        [0,  0,  0,  0,  0,  0,  0,  0], 
        [0,  1,  0,  0,  0,  0,  0,  1], 
        [1,  0,  0,  0,  0,  0,  0,  1], 
        [0,  1,  1,  0,  0,  1,  1,  0]  
    ]
    return(adMatrix)

"""
count = foo2()[7].count(1)
print(count)
"""
"""
count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0

lis = foo2()


for i in range(len(lis)):

    count0 += int(lis[i][0])
    count1 += int(lis[i][1])
    count2 += int(lis[i][2])
    count3 += int(lis[i][3])
    count4 += int(lis[i][4])
    count5 += int(lis[i][5])
    count6 += int(lis[i][6])
    count7 += int(lis[i][7])

print(count0, count1, count2, count3, count4, count5, count6, count7)
"""
def bar2():
    adList = [
        [1,  3,  6],
        [0,  5,  7],
        [7],
        [0],
        [],
        [1,  7],
        [0,  7],
        [1,  2,   5,   6]
    ]
    return(adList)

def qux2(adlis, int1, int2):

    if adlis[int1][int2] == 1:
        adlis[int1].pop(int2)
        adlis[int2].pop(int1)

    return(adlis)

def aap2(adlis, int1, int2):

    if adlis[int1][int2] == 0:
        adlis[int1].pop(int2)
        adlis[int2].pop(int1)

        adlis[int1].insert(int2, 1)
        adlis[int2].insert(int1, 1)

    return(adlis)

def ham2(adlis, int1, int2):

    if int2 in adlis[int1]:
        adlis[int1].remove(int2)
        adlis[int2].remove(int1)

    return(adlis)

def egg2(adlis, int1, int2):

    if int2 not in adlis[int1]:
        adlis[int1].insert(int2)
        adlis[int2].insert(int1)

    return(adlis)

#print(egg2(bar2(), 3, 6))

lis = [1,2,3,4,5,6,7]

#print([index for index, value in enumerate(lis) if value > 5])

def fooo(ham, egg, gzk, qux):
    gzk = not gzk
    ham += 87 

    for i in range(ham):
        print("SHINTO")
    ham = ham * 63
    print(gzk, qux, sep = ", ")

fooo(1, 56, True, False)
"""
print("Hello")
for i in range(1, 19):
    print(i)
"""
"""
lis1 = [x for x in range(100)]
lis2 = [x for x in range(10, 8587, 2)]

print(lis1)
print()
print(lis2)
print()

lis2 = lis2 + lis1
print(lis2)
print()
for i in range(20):
    lis2.insert(20, 48)
print(lis2)

for i in range(30):
    lis2.insert(0, "DAINTY")

for i in range(19):
    lis2.pop(-1)

print()
print(lis2)"""