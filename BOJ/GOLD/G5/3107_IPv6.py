import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

IP_infos = input().strip().split(':')
ans = ''

skip_next = False
for i in range(len(IP_infos)):
    IP_info = IP_infos[i]

    if skip_next:
        skip_next = False
        continue

    length = len(IP_info)

    if IP_info == '':
        if i == 0 and IP_infos[1] == '':
            ans += '0000:' * (10 - len(IP_infos))
            skip_next = True
        elif i == 0 or i == len(IP_infos) - 1:
            ans += '0000:'
        else:
            ans += '0000:' * (9 - len(IP_infos))
    else:
        ans += '0' * (4-length) + IP_info + ':'


print(ans[:-1])
