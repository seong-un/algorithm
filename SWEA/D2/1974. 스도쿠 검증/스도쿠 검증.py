T = int(input())
for test_case in range(1, T + 1):
    sudoku=[]
    result=1
    for i in range(9):
        sudoku.append(list(map(int, input().split())))
    for j in range(9):
        for i in range(1,10,1):
            if i not in sudoku[j]:
                result=0
    for j in range(9):
        for i in range(1,10,1):
            if i not in [k[j] for k in sudoku]:
                result=0
    for i in range(3):
        for j in range(3):
            for k in range(1,10,1):
                if k not in [sudoku[3*i][3*j], sudoku[3*i][3*j+1], sudoku[3*i][3*j+2], sudoku[3*i+1][3*j], sudoku[3*i+1][3*j+1], sudoku[3*i+1][3*j+2], sudoku[3*i+2][3*j], sudoku[3*i+2][3*j+1], sudoku[3*i+2][3*j+2]]:
                    result=0
    print(f"#{test_case} {result}")