def rules(i,x):
    
    #RuleRow 
    RuleRow=all(puzzle[i][x]!=puzzle[i][y] 
                    for y in range(9)
                    if x!=y 
                )
    print(RuleRow)

    #RuleCol
    RuleCol=all(puzzle[i][x]!=puzzle[j][x] 
                       for y in range(9)
                       for j in range(9)
                       if i!=j
                )
    print(RuleCol)
    
    #RuleBox
    RuleBox=all(puzzle[i][x]!=puzzle[j][y]
                for j in range(9)
                for y in range(9)
                if (i!=j or x!=y) and i//3 == j//3 and x//3 ==y//3
            ) 
    print(RuleBox)

    Rules = RuleRow and RuleCol and RuleBox
    return Rules

puzzle =   [[5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]]

print(rules(0,0))