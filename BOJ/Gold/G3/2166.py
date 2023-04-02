import sys
input = sys.stdin.readline

N = int(input())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

matrix.append((matrix[0][0], matrix[0][1]))

result = 0
for i in range(N):
    result += matrix[i][0] * matrix[i+1][1]
    result -= matrix[i][1] * matrix[i+1][0]

print(round(abs(result/2), 1))
