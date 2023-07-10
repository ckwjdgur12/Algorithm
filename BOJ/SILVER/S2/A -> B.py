import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def back_tracking(start, depth):

    if start > B:
        return

    if start == B:
        ansLst.append(depth)

    back_tracking(start*2, depth+1)
    back_tracking((start*10)+1, depth+1)


ansLst = []
A, B = map(int, input().split())
back_tracking(A, 1)

if ansLst: print(min(ansLst))
else: print(-1)
