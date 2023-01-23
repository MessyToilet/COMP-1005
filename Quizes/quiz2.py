def adjacency_matrix():

    ad_matrix = [
        
        [0,  0,  0,  0,  1,  0,  0,  0 ],
        [0,  0,  1,  0,  1,  0,  0,  0 ],
        [0,  0,  0,  0,  0,  0,  0,  0 ],
        [0,  0,  0,  0,  1,  0,  0,  0 ],
        [1,  0,  0,  0,  0,  0,  1,  0 ],
        [0,  0,  0,  1,  0,  0,  0,  1 ],
        [0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  1,  0,  0,  0,],
    ]
    return(ad_matrix)

def print_edges(matrix):
    for row in range(len(matrix)):
        edges = matrix[row].count(1)
        print(edges, end = ", ")

    out_of_two = matrix[2].count(1)
    print(f"\n{out_of_two}")



#print_edges(adjacency_matrix())

def func(gzk, shm, foo, bar, ukr):
    shm = not shm 
    gzk *= 5 
    gzk *= 97
    counter = foo
    while counter <= 120:
        print(chr(counter))
        counter += 1
    print(gzk, ukr, shm, foo, bar, sep = "; ")

#func(5, True, 100, True, True)

lis = [x for x in range(100)]
def func2(gzk):
    newlis = gzk[14:-17:]

    
    for i in range(17):
        newlis.insert(11, 40)


    for i in range(14):
        newlis.pop(0)

    for i in range(len(newlis)):
        try:
            newlis.remove(58)
        except:
            break
    return(newlis)
    
def func3(foo, ham, xyz, aap, bar, ukr):
    egg = ham * 77
    ham *= 39 
    foo = not foo
    aap += 18
    if (foo or xyz):
        ham *= 76
    return(egg, bar, aap, xyz)

print(func3(True, 5, False, 5, .5, .5))
