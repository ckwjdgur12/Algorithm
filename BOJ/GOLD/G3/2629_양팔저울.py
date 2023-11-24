import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")


def dfs(idx, left, right):

    w = abs(right - left)
    result.add(w)

    if idx == N: return

    if not visited[idx][w]:
        dfs(idx+1, left+weights[idx], right)
        dfs(idx+1, left, right+weights[idx])
        dfs(idx+1, left, right)
        visited[idx][w] = True

    return


N = int(input())
weights = list(map(int, input().split()))
weights.sort()
M = int(input())
marbles = list(map(int, input().split()))

visited = list([False] * 15001 for _ in range(N))

result = set()
dfs(0, 0, 0)

ans = []
for marble in marbles:
    if marble in result: ans.append("Y")
    else: ans.append("N")

print(*ans)
