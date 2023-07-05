import sys
import bisect
import math
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

# def findParent(x):
#     if parent[x] != x:
#         parent[x] = findParent(parent[x])
#     return parent[x]

# def unionParent(x, y):
#     x = findParent(x)
#     y = findParent(y)
#     parent[x] = y


# N, M, K = map(int, input().split())

# myCards = list(map(int, input().split()))
# opponentCards = list(map(int, input().split()))
# parent = list(i for i in range(len(myCards)+1))

# myCards.sort()
# for opponentCard in opponentCards:
#     nextCard = opponentCard + 1

#     idx = bisect.bisect_left(myCards, nextCard)

#     value = findParent(idx)
#     print(myCards[value])
#     unionParent(value, value+1)



N, M, K = map(int, input().split())

myCards = list(map(int, input().split()))
opponentCards = list(map(int, input().split()))
idxNum = int(math.sqrt(50000)) + 1
check = [False] * 4000001
dummy = [0] * idxNum

for myCard in myCards:
    check[myCard] = True
    dummy[myCard // idxNum] += 1

for opponentCard in opponentCards:
    nextCard = opponentCard + 1

    while dummy[nextCard // idxNum] == 0:
        nextCard = (nextCard + idxNum) - (nextCard % idxNum)

    for i in range(nextCard, N+1):
        if check[i]:
            check[i] = False
            dummy[i // idxNum] -= 1
            print(i)
            break
