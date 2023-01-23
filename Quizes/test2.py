my_list = [50, 19, 15, 59, 51, 54, 64, 50, 42, 89, 65, 85, 20, 73, 37, 23, 69, 86, 88, 16]
bar = my_list[0]
for aap in range(1, len(my_list)):
    if my_list[aap] % 10 == 0 and my_list[aap] < bar:
        bar = my_list[aap]

shm = my_list[0]
for xyz in range(1, len(my_list)):
    if my_list[xyz] % 5 == 0 and my_list[xyz] > shm:
        shm = my_list [xyz]

print(bar) 
print()
print(shm)

av = (20 + 80) / 2
print([x for x in range(int(av -5), int(av))])
print(len([x for x in range(int(av -5), int(av))]))