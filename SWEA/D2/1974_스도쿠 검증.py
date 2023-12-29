import sys

sys.stdin = open("BOJ/input.txt", "r")


T = int(input())
for test_case in range(1, T+1):
    
    sudoku = list(list(map(int, input().split())) for _ in range(9))
    wrong = False

    for i in range(9):
        validation_set = set(sudoku[i])
        if len(validation_set) != 9:
            wrong = True
            break

        validation_set = set()
        for j in range(9): 
            validation_set.add(sudoku[j][i])
        if len(validation_set) != 9:
            wrong = True
            break

        validation_set = set()
        for j in range(9):
            validation_set.add(sudoku[j//3 + (i//3)*3][j%3 + (i%3)*3])
        if len(validation_set) != 9:
            wrong = True
            break

    if wrong: print(f'#{test_case} 0')
    else: print(f'#{test_case} 1')
