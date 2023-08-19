import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def make_strings():
    if find_string("()"): strings.append("()")
    else: return

    for i in range(4, len(S)+1, 2):
        for s in strings:
            L = len(s)
            if (i-2) % L != 0: continue

            tmp_str = "(" + s * ((i-2) // L) + ")"

            if find_string(tmp_str): strings.append(tmp_str)
    
    strings.sort()
    return


def find_string(string):
    idx = 0
    L = len(string)    
    for c in S:
        if c == string[idx]: 
            idx += 1
            if idx == L: return True

    return False


S = list(input().strip())
K = int(input())

strings = []

make_strings()

if len(strings) < K: print(-1)
else: print(strings[K-1])
