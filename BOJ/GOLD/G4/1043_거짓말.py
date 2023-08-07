import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

N, M = map(int, input().split())
ppl = list(map(int, input().split()[1:]))
ppl = set(ppl)

parties = []
for _ in range(M):
    seq = set(map(int, input().split()[1:]))
    parties.append(seq)

for _ in range(M):
    for party in parties:
        if party & ppl:
            ppl |= party

ans = 0
for party in parties:
    if not party & ppl:
        ans += 1

print(ans)
