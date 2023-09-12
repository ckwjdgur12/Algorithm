import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def dfs(idx):
    global C_cnt, B_cnt, A_cnt
    if C_cnt > (seq_length + 4 - idx) // 3: return
    if B_cnt > (seq_length + 3 - idx) // 2: return

    if idx == len(seq) + 2: return True

    if C_cnt > 0 and string[idx-1] != 'C' and string[idx-2] != 'C':
        C_cnt -= 1
        string[idx] = 'C'
        if dfs(idx+1): return True
        string[idx] = None
        C_cnt += 1

    if B_cnt > 0 and string[idx-1] != 'B':
        B_cnt -= 1
        string[idx] = 'B'
        if dfs(idx+1): return True
        string[idx] = None
        B_cnt += 1

    if A_cnt > 0:
        A_cnt -= 1
        string[idx] = 'A'
        if dfs(idx+1): return True
        string[idx] = None
        A_cnt += 1

    return False


seq = list(input().strip())
seq_length = len(seq)
A_cnt = seq.count('A')
B_cnt = seq.count('B')
C_cnt = seq.count('C')

string = [None] * (len(seq) + 2)

if dfs(2): print(''.join(string[2:]))
else: print(-1)
