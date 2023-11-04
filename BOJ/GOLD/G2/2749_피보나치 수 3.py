import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

MOD = 1000000
P = MOD//10 * 15
fibo = [0] * (P+1)
fibo[1] = 1

n = int(input())
for i in range(2, P+1):
    fibo[i] = fibo[i-1] + fibo[i-2]
    fibo[i] %= MOD

print(fibo[n%P])
