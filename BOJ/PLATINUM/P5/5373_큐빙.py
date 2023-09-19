import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

U, D, F, B, L, R = 0, 1, 2, 3, 4, 5
color = {0:'w', 1:'y', 2:'r', 3:'o', 4:'g', 5:'b'}
# color = {0:'w', 1:'y', 2:'g', 3:'b', 4:'o', 5:'r'} #debug

def init_cube():
    for i in range(0, 6):
        for j in range(3):
            for k in range(3):
                cube[i][j][k] = color[i]
    return


def exec_face(side, dir):
    if dir == '-':
        f_elem = cube[side][0][0]
        s_elem = cube[side][0][1]

        for i in range(2): cube[side][0][i] = cube[side][i][-1]
        for i in range(2): cube[side][i][-1] = cube[side][-1][-(i+1)]
        for i in range(2): cube[side][-1][-(i+1)] = cube[side][-(i+1)][0]
        
        cube[side][2][0] = f_elem
        cube[side][1][0] = s_elem
    else:
        f_elem = cube[side][0][1]
        s_elem = cube[side][0][2]

        for i in range(2): cube[side][0][-(i+1)] = cube[side][i][0]
        for i in range(2): cube[side][i][0] = cube[side][-1][i]
        for i in range(2): cube[side][-1][i] = cube[side][-(i+1)][-1]
        cube[side][1][-1] = f_elem
        cube[side][2][-1] = s_elem
    return


def exec_top_bottom_side(side, dir):
    if side == U: pos = 0
    else:
        if dir == '-': dir = '+'
        else: dir = '-'
        pos = 2

    if dir == '-':
        first_side_elem = list(cube[F][pos])
        sides = [F, L, B, R]

        for i in range(3):
            for j in range(3):
                cube[sides[i]][pos][j] = cube[sides[i+1]][pos][j]
        for j in range(3): 
            cube[sides[3]][pos][j] = first_side_elem[j]
    else:
        first_side_elem = list(cube[F][pos])
        sides = [F, R, B, L]

        for i in range(3):
            for j in range(3):
                cube[sides[i]][pos][j] = cube[sides[i+1]][pos][j]
        for j in range(3):
            cube[sides[3]][pos][j] = first_side_elem[j]

    return


def exec_front_back_side(side, dir):

    if side == F: first, last = 0, -1
    else:
        if dir == '-': dir = '+'
        else: dir = '-'
        first, last = -1, 0

    if dir == '-':
        sides = [U, R, D, L]
        first_side_elem = list(cube[sides[0]][last])
        for i in range(3):
            cube[sides[0]][last][i] = cube[sides[1]][i][first]
        for i in range(3):
            cube[sides[1]][i][first] = cube[sides[2]][first][-(i+1)]
        for i in range(3):
            cube[sides[2]][first][i] = cube[sides[3]][i][last]
        for i in range(3):
            cube[sides[3]][i][last] = first_side_elem[-(i+1)]
    else:
        sides = [U, L, D, R]
        first_side_elem = list(cube[sides[0]][last])
        for i in range(3):
            cube[sides[0]][last][i] = cube[sides[1]][-(i+1)][last]
        for i in range(3):
            cube[sides[1]][i][last] = cube[sides[2]][first][i]
        for i in range(3):
            cube[sides[2]][first][i] = cube[sides[3]][-(i+1)][first]
        for i in range(3):
            cube[sides[3]][i][first] = first_side_elem[i]

    return


def exec_left_right_side(side, dir):

    if side == L: first, last = 0, -1
    else:
        if dir == '-': dir = '+'
        else: dir = '-'
        first, last = -1, 0

    if dir == '-':
        sides = [U, F, D, B]
        first_side_elem = [cube[sides[0]][0][first], cube[sides[0]][1][first], cube[sides[0]][2][first]]
        for i in range(3):
            cube[sides[0]][i][first] = cube[sides[1]][i][first]
        for i in range(3):
            cube[sides[1]][i][first] = cube[sides[2]][i][first]
        for i in range(3):
            cube[sides[2]][i][first] = cube[sides[3]][-(i+1)][last]
        for i in range(3):
            cube[sides[3]][i][last] = first_side_elem[-(i+1)]
    else:
        sides = [U, B, D, F]
        first_side_elem = [cube[sides[0]][0][first], cube[sides[0]][1][first], cube[sides[0]][2][first]]
        for i in range(3):
            cube[sides[0]][i][first] = cube[sides[1]][-(i+1)][last]
        for i in range(3):
            cube[sides[1]][i][last] = cube[sides[2]][-(i+1)][first]
        for i in range(3):
            cube[sides[2]][i][first] = cube[sides[3]][i][first]
        for i in range(3):
            cube[sides[3]][i][first] = first_side_elem[i]

    return


def exec_op(side, dir):
    if side == 'U': 
        exec_face(U, dir)
        exec_top_bottom_side(U, dir)
    elif side == 'D': 
        exec_face(D, dir)
        exec_top_bottom_side(D, dir)
    elif side == 'F': 
        exec_face(F, dir)
        exec_front_back_side(F, dir)
    elif side == 'B': 
        exec_face(B, dir)
        exec_front_back_side(B, dir)
    elif side == 'L': 
        exec_face(L, dir)
        exec_left_right_side(L, dir)
    else: 
        exec_face(R, dir)
        exec_left_right_side(R, dir)
    return


def print_result():
    # for i in [0, 1, 4, 2, 5, 3]:
    #     print(color[i])
    for j in range(3):
        print(''.join(cube[U][j]))
    #print()
    return


cube = list(list([0] * 3 for _ in range(3)) for _ in range(6))

T = int(input())
for _ in range(T):
    n = int(input())
    operates = list(input().split())

    init_cube()

    for op in operates:
        exec_op(op[0], op[1])

    print_result()
    