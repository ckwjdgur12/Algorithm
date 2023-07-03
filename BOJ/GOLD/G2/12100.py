import sys
from copy import deepcopy

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
result = 0


def LEFT(brd):
    v = [[False] * N for _ in range(N)]
    for j in range(N):
        for k in range(1, N):
            if brd[j][k] == 0: continue # 빈 공간이면 넘어감

            idx = k
            if brd[j][k-1] == 0:    # 움직일 다음칸이 0이면 숫자를 만날때까지 이동
                idx -= 1
                while brd[j][idx] == 0 and idx >= 0:
                    idx -= 1
                idx += 1
                brd[j][k], brd[j][idx] = brd[j][idx], brd[j][k]

            if idx == 0: continue   # 끝까지 갔다면 리턴

            if brd[j][idx] == brd[j][idx-1] and not v[j][idx-1]:    # 합친 후 공간이 남아있다면 밀어줌?? 공간이 남아있으면 안되지ㄹㅇㅋㅋ
                brd[j][idx-1] *= 2
                brd[j][idx] = 0
                v[j][idx-1] = True
    
    return brd


def UP(brd):
    v = [[False] * N for _ in range(N)]
    for j in range(N):
        for k in range(1, N):
            if brd[k][j] == 0: continue # 빈 공간이면 넘어감

            idx = k
            if brd[k-1][j] == 0:    # 움직일 다음칸이 0이면 숫자를 만날때까지 이동
                idx -= 1
                while brd[idx][j] == 0 and idx >= 0:
                    idx -= 1
                idx += 1
                brd[k][j], brd[idx][j] = brd[idx][j], brd[k][j]

            if idx == 0: continue   # 끝까지 갔다면 리턴

            if brd[idx][j] == brd[idx-1][j] and not v[idx-1][j]:    # 합친 후 공간이 남아있다면 밀어줌?? 공간이 남아있으면 안되지ㄹㅇㅋㅋ
                brd[idx-1][j] *= 2
                brd[idx][j] = 0
                v[idx-1][j] = True

    return brd


def RIGHT(brd):
    v = [[False] * N for _ in range(N)]
    for j in range(N):
        for k in range(2, N+1):
            if brd[j][-k] == 0: continue # 빈 공간이면 넘어감

            idx = -k
            if brd[j][-k+1] == 0:    # 움직일 다음칸이 0이면 숫자를 만날때까지 이동
                idx += 1
                while brd[j][idx] == 0 and idx < 0:
                    idx += 1
                idx -= 1
                brd[j][-k], brd[j][idx] = brd[j][idx], brd[j][-k]

            if idx == -1: continue   # 끝까지 갔다면 리턴

            if brd[j][idx] == brd[j][idx+1] and not v[j][idx+1]:    # 합친 후 공간이 남아있다면 밀어줌?? 공간이 남아있으면 안되지ㄹㅇㅋㅋ
                brd[j][idx+1] *= 2
                brd[j][idx] = 0
                v[j][idx+1] = True
    
    return brd


def DOWN(brd):
    v = [[False] * N for _ in range(N)]
    for j in range(N):
        for k in range(2, N+1):
            if brd[-k][j] == 0: continue # 빈 공간이면 넘어감

            idx = -k
            if brd[-k+1][j] == 0:    # 움직일 다음칸이 0이면 숫자를 만날때까지 이동
                idx += 1
                while brd[idx][j] == 0 and idx < 0:
                    idx += 1
                idx -= 1
                brd[-k][j], brd[idx][j] = brd[idx][j], brd[-k][j]

            if idx == -1: continue   # 끝까지 갔다면 리턴

            if brd[idx][j] == brd[idx+1][j] and not v[idx+1][j]:    # 합친 후 공간이 남아있다면 밀어줌?? 공간이 남아있으면 안되지ㄹㅇㅋㅋ
                brd[idx+1][j] *= 2
                brd[idx][j] = 0
                v[idx+1][j] = True
    
    return brd


def backTracking(depth, board):
    global result

    if depth == 5:  # 5번 실행했다면 최대값 찾아서 갱신하기
        maxSize = 0
        for i in range(N):
            maxSize = max(maxSize, max(board[i]))
        result = max(maxSize, result)
        return
    
    functions = [LEFT, RIGHT, UP, DOWN]
    for function in functions:
        brd = deepcopy(board)
        brd = function(brd)
        backTracking(depth+1, brd)


backTracking(0, graph)
print(result)



'''
for i in range(N):
    print(graph[i])
print()
RIGHT(graph, visited)
for i in range(N):
    print(graph[i])
print()
visited = [[False] * N for _ in range(N)]

UP(graph, visited)
for i in range(N):
    print(graph[i])
print()
visited = [[False] * N for _ in range(N)]

RIGHT(graph, visited)
for i in range(N):
    print(graph[i])
print()
visited = [[False] * N for _ in range(N)]

UP(graph, visited)
for i in range(N):
    print(graph[i])
print()
visited = [[False] * N for _ in range(N)]

RIGHT(graph, visited)
for i in range(N):
    print(graph[i])
print()
'''
