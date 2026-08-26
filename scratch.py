def rules(puzzle):
    #sudoku rules:
    # puzzle[i][x] in range(10) for i, x in range(10) --> RuleNum
    # puzzle[i][x]!=puzzles[i][y] for i, x, y in range(10) // keine doppelte Zahl pro Reihe --> RuleRow
    # puzzle[i][x]!=puzzles[j][x] for i, j, x in range(10) // keine doppelte Zahl pro Spalte --> RuleCol
    # puzzle[i][x]!=puzzles[j][y] for i //3 == j//3 and x//3 ==y//3 //keine doppelte Zahl in 3x3 Quadrant --> RuleBox
    
    #RuleNum:
    RuleNum=all(puzzle[i][x] in range(10)
                for i in range(9)
                for x in range(9)
    )
    
    #RuleRow
    RuleRow=all(puzzle[i][x]!=puzzle[i][y] or puzzle[i][x]==0
                    for i in range(9)
                    for x in range(9)
                    for y in range(9)
                    if x!=y
    )
    
    #RuleCol
    RuleCol=all(puzzle[i][x]!=puzzle[j][x] or puzzle[i][x]==0
                        for i in range(9)
                        for j in range(9)
                        for x in range(9)
                        if i!=j
    )

    #RuleBox
    RuleBox=all(puzzle[i][x]!=puzzle[j][y] or puzzle[i][x]==0
                for i in range(9)
                for j in range(9)
                for x in range(9)
                for y in range(9)
                if (i!=j or x!=y) and i//3 == j//3 and x//3 ==y//3
            ) 

    Rules = RuleNum and RuleRow and RuleCol and RuleBox
    return Rules

def candidates(puzzle):
    options=0
    optionsMatrix = []
    for i in range(9):
        for x in range(9):
            if puzzle[i][x]==0: 
                for test in range(1,10):
                    puzzle[i][x]=test   
                    if rules(puzzle):
                        options+=1
                optionsMatrix.append([i,x,options])
                puzzle[i][x]=0
                options=0
    bestCandidates= sorted(optionsMatrix, key= lambda mat: mat[2])
    return bestCandidates

def sudoku(puzzle):

    bestCandidates = candidates(puzzle)
    steps = len(bestCandidates) 

    for i in range(steps):
        bestCandidates=candidates(puzzle)
        if not bestCandidates:
            break
        for el in bestCandidates:
            if el[2]==1: #guaranteedto exist by rules
                for test in range(1,10):
                    puzzle[el[0]][el[1]]=test
                    if rules(puzzle):
                        break
    return puzzle
    


 

         






puzzle =   [[5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]]

print(rules(puzzle))
print(sudoku(puzzle))