import sys
import math
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")
mod = 1000000007

def get_power(num, pow):
    if pow == 1:
        return num
    
    value = (get_power(num, pow//2))
    if pow % 2 == 0:
        return value * value % mod
    else:
        return value * value * num % mod


def get_value(a, b):
    value = (b * get_power(a, mod-2)) % mod
    return value


M = int(input())

ans = 0
for _ in range(M):
    N, S = map(int, input().split())
    gcd = math.gcd(N, S)
    N //= gcd
    S //= gcd

    ans += get_value(N, S)
    ans %= mod

print(ans)
