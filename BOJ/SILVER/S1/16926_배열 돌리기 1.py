import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def get_elems(i):
    for j in range(i, M-1-i):
        elems.append(arr[i][j])
    for j in range(i, N-1-i):
        elems.append(arr[j][-i-1])
    for j in range(M-1-i, i, -1):
        elems.append(arr[-i-1][j])
    for j in range(N-1-i, i, -1):
        elems.append(arr[j][i])
    return


N, M, R = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(N))
ans = list([None] * M for _ in range(N))

cycle = min(N, M) // 2

for i in range(cycle):
    cycle_elems_cnt = 2 * ((N-2*i) + (M-2*i)) - 4
    backward_cnt = R % cycle_elems_cnt
    elems = []
    
    get_elems(i)

    for k in range(cycle_elems_cnt):
        cnt = (backward_cnt - k) % cycle_elems_cnt
        elem = elems[k]

        row_c = N - 2*i
        col_c = M - 2*i

        if cnt == 0:
            ans[i][i] = elem
        elif cnt < row_c:
            ans[cnt+i][i] = elem
        elif row_c <= cnt < row_c + col_c - 1:
            ans[-i-1][cnt - row_c + 1 + i] = elem
        elif row_c + col_c - 1 <= cnt <  2*row_c + col_c - 2:
            ans[(2*row_c+col_c - 3) - cnt + i][-i-1] = elem
        else:
            ans[i][-(cnt - (2*row_c+col_c-3)) - 1 - i] = elem

for a in ans:
    print(*a)



# cycle = min(N, M) // 2

# for _ in range(R):
#     for i in range(cycle):
#         first_elem = arr[i][i]

#         for j in range(i, M-1-i):
#             arr[i][j] = arr[i][j+1]
#         for j in range(i, N-1-i):
#             arr[j][-i-1] = arr[j+1][-i-1]
#         for j in range(M-1-i, i, -1):
#             arr[-i-1][j] = arr[-i-1][j-1]
#         for j in range(N-1-i, i+1, -1):
#             arr[j][i] = arr[j-1][i]
#         arr[i+1][i] = first_elem

# for a in arr:
#     print(*a)
