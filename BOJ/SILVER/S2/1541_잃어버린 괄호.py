import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

string = list(input().split('-'))

ans = 0
first = True
for s in string:
    tmp_sum = 0
    tmp_str = s.split('+')
    
    for tmp_s in tmp_str:
        tmp_sum += int(tmp_s)

    if not first: ans -= tmp_sum
    else: 
        ans += tmp_sum
        first = False

print(ans)
