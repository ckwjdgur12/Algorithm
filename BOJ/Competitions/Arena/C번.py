import sys
input = sys.stdin.readline
# sys.stdin = open("BOJ/input.txt", "r")

output = []
for _ in range(100):
    output.append('2')

win_cnt = int(input())

for i in range(100):
    output[i] = '0'
    print('? ' + ''.join(output), flush=True)
    next_win_cnt = int(input())
    
    if next_win_cnt == win_cnt:
        output[i] = '5'
        win_cnt += 1
    elif next_win_cnt > win_cnt:
        win_cnt += 1
    else:
        output[i] = '2'
    
print('! ' + ''.join(output), flush=True)
