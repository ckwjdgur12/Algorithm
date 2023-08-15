import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def init_sudoku():
    for _ in range(N):
        U, LU, V, LV = input().split()
        U_x, U_y = ord(LU[0]) - ord('A'), int(LU[1]) - 1
        V_x, V_y = ord(LV[0]) - ord('A'), int(LV[1]) - 1
        A[U_x][U_y], A[V_x][V_y] = int(U), int(V)
        Visit[int(U) - 1][int(V) - 1], Visit[int(V) - 1][int(U) - 1] = 1, 1
        R[U_x][int(U) - 1], R[V_x][int(V) - 1] = 1, 1
        C[U_y][int(U) - 1], C[V_y][int(V) - 1] = 1, 1
        S[U_x // 3 * 3 + U_y // 3][int(U) - 1] = 1
        S[V_x // 3 * 3 + V_y // 3][int(V) - 1] = 1

    for i, pos in enumerate(input().split()):
        pos_x, pos_y = ord(pos[0]) - ord('A'), int(pos[1]) - 1
        A[pos_x][pos_y] = i + 1
        R[pos_x][i], C[pos_y][i] = 1, 1
        S[pos_x // 3 * 3 + pos_y // 3][i] = 1

    return


def get_poses():
    for r in range(9):
        for c in range(9):
            if not A[r][c]:
                E.append([r, c])
    return


def sudoku_validation(i, j, r, c, pair_x, pair_y):
    if (R[r][i] == R[pair_x][j] == C[c][i] == C[pair_y][j] 
        == S[r // 3 * 3 + c // 3][i] == S[pair_x // 3 * 3 + pair_y // 3][j] == 0):
        return True
    return False


def set_visited(i, j, r, c, pair_x, pair_y, TF):

    if TF:
        A[r][c], A[pair_x][pair_y] = i + 1, j + 1
    else:
        A[r][c], A[pair_x][pair_y] = 0, 0
        

    Visit[i][j], Visit[j][i] = TF, TF
    R[r][i], R[pair_x][j], C[c][i], C[pair_y][j], S[r // 3 * 3 + c // 3][i], S[
    pair_x // 3 * 3 + pair_y // 3][j] = TF, TF, TF, TF, TF, TF
    return


def back_tracking(cnt, itr):
    find = False

    if cnt == Ecnt:
        print(f'Puzzle {itr}')
        for a in A:
            print("".join(map(str, a)))
        return True
    
    r, c = E[cnt]
    if A[r][c]:
        find = back_tracking(cnt + 1, itr)
        return find
    
    for i in range(9):
        for j in range(9):
            if i == j or Visit[i][j]: continue

            for d in dr:
                pair_x, pair_y = r + d[0], c + d[1]
                if not (0 <= pair_x <= 8 and 0 <= pair_y <= 8): continue
                if A[pair_x][pair_y]: continue
                if not sudoku_validation(i, j, r, c, pair_x, pair_y): continue

                set_visited(i, j, r, c, pair_x, pair_y, 1)

                find = back_tracking(cnt + 1, itr)
                if find:
                    return find
                
                set_visited(i, j, r, c, pair_x, pair_y, 0)

    return find


itr = 1
while True:
    N = int(input())
    dr = [[0, 1], [1, 0]]

    if N == 0:
        break

    A = [[0] * 9 for _ in range(9)]
    Visit = [[0] * 9 for _ in range(9)]
    R = [[0] * 9 for _ in range(9)]
    C = [[0] * 9 for _ in range(9)]
    S = [[0] * 9 for _ in range(9)]
    E = []

    init_sudoku()

    get_poses()

    Ecnt = len(E)

    back_tracking(0, itr)

    itr += 1
