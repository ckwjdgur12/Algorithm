import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

num = 0

def recursion(n, r, c):
    global num

    if n == 1:
        if r == 0 and c == 0: return num
        if r == 0 and c == 1: return num + 1
        if r == 1 and c == 0: return num + 2
        if r == 1 and c == 1: return num + 3

    quarter = (2**(n*2) // 4)
    set_pos = (2**(n-1))

    if r < 2**(n-1) and c < 2**(n-1):
        return recursion(n-1, r, c)
    elif r < 2**(n-1) and c >= 2**(n-1):
        num += quarter
        return recursion(n-1, r, c-set_pos)
    elif r >= 2**(n-1) and c < 2**(n-1):
        num += quarter * 2
        return recursion(n-1, r-set_pos, c)
    else:
        num += quarter * 3
        return recursion(n-1, r-set_pos, c-set_pos)

N, r, c = map(int, input().split())

print(recursion(N, r, c))
