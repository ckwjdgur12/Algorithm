import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def get_coordinates(elem):
    min_x, min_y = 51, 51
    max_x, max_y = -1, -1

    for i in range(N):
        for j in range(M):
            if grid[i][j] == elem:
                min_x = min(min_x, i)
                min_y = min(min_y, j)
                max_x = max(max_x, i)
                max_y = max(max_y, j)

    return min_x, min_y, max_x, max_y


def set_graph(elem, coordinates):
    min_x, min_y, max_x, max_y = coordinates
    checked_elem = set()

    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            if grid[i][j] == '.':
                print(-1)
                exit(0)
            elif grid[i][j] != elem and grid[i][j] not in checked_elem:
                indegree[grid[i][j]] += 1
                checked_elem.add(grid[i][j])
                graph[elem].append(grid[i][j])
    return


def check(elem):
    coordinates = get_coordinates(elem)

    set_graph(elem, coordinates)

    return


def topological_sort():
    indegree_lst = sorted(indegree.items(), key = lambda x:(x[1], x[0]))
    
    while indegree_lst:
        key, value = indegree_lst[0]
        del indegree[key]
        if value != 0:
            print(-1)
            exit(0)

        ans.append(key)

        for next in graph[key]:
            indegree[next] -= 1
        
        indegree_lst = sorted(indegree.items(), key = lambda x:(x[1], x[0]))

    return


N, M = map(int, input().split())
grid = list(input().strip() for _ in range(N))

sand_box = [[0] * M for _ in range(N)]
indegree = {}
graph = {}

for i in range(N):
    for j in range(M):
        if grid[i][j] not in graph and grid[i][j] != '.':
            graph[grid[i][j]] = []
            indegree[grid[i][j]] = 0

checked_elem = set()
checked_elem.add('.')

for i in range(N):
    for j in range(M):
        if grid[i][j] not in checked_elem:
            elem = grid[i][j]
            checked_elem.add(elem)
            check(elem)

ans = []
topological_sort()
print("".join(ans))
