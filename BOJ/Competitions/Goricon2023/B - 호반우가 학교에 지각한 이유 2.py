import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

A, B, N = map(int, input().split())

def make_prime():
    global idx_len

    result = ""
    result += str(A)

    if A%10 == 9:
        result += "7"
        idx_len -= 1

    result += "1" * idx_len
    result += str(B)

    return result


prime = [True] * 100
for i in range(2, 100):
    num = i*2
    while num < 100:
        prime[num] = False
        num += i

idx = 2
idx_len = N - 4

if not prime[A]: print(-1)
elif not prime[B]: print(-1)
elif (B//10) % 2 == 0: print(-1)
elif (B//10) == 5: print(-1)
else:
    print(make_prime())

