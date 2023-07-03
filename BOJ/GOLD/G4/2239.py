import sys
input = sys.stdin.readline

sudoku = []
reverse_sudoku = [[0] * 9 for _ in range(9)]
area = [[] for _ in range(9)]
zeroPos = []

def backTracking(depth):
    if len(zeroPos) == depth:   # 모든 0에 대하여 처리했다면 출력
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j], end="")
            print()
        exit(0)

    x, y = zeroPos[depth]
    for k in range(1, 10):
        if k in sudoku[x]: continue     # 가능여부 확인
        if k in reverse_sudoku[y]: continue
        if k in area[(x//3)*3+(y//3)]: continue

        sudoku[x][y] = k    # 업데이트
        reverse_sudoku[y][x] = k
        area[(x//3)*3+(y//3)][(x%3)*3+(y%3)] = k
        backTracking(depth+1)   # backTracking!
        sudoku[x][y] = 0    # 되돌리기
        reverse_sudoku[y][x] = 0
        area[(x//3)*3+(y//3)][(x%3)*3+(y%3)] = 0


for _ in range(9):
    sudoku.append(list(input().strip()))

for i in range(9):
    for j in range(9):
        sudoku[i][j] = int(sudoku[i][j])                # 스도쿠 원소들 int로 변환
        reverse_sudoku[j][i] = sudoku[i][j]             # row, col 뒤집은 스도쿠 판
        area[(i//3)*3+(j//3)].append(sudoku[i][j])      # 3x3 정보를 담은 area
        if sudoku[i][j] == 0: zeroPos.append((i, j))    # 0인 좌표들 저장

backTracking(0)

