import sys
import math
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

N, M, K = map(int, input().split())

myCards = list(map(int, input().split()))
opponentCards = list(map(int, input().split()))
idxNum = int(math.sqrt(4000000)) + 1
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
