def move_zeros(lst):
    cleaner=[el for el in lst if el !=0]
    print(cleaner)
    for i in range (len(lst)-len(cleaner)):
        cleaner.append(0)
        i+=1
    return cleaner




test=[1, 2, 0, 1, 0, 1, 0, 3, 0, 1]

print(move_zeros(test))