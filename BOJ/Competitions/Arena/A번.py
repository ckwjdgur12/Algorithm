import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
seq.insert(0, 0)

for q in range(int(input())):
    q = list(map(int, input().split()))
    
    if q[0] == 1:
        qn, l, r, k = q
        print(seq[l:r+1].count(k))
    else:
        qn, l, r = q
        for i in range(l, r+1):
            seq[i] = 0



