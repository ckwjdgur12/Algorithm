import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

ip = [255, 255, 255, 255]
min_ip = [256, 256, 256, 256]
max_ip = [-1, -1, -1, -1]
input_ips = []
for _ in range(int(input())):
    input_ips.append(list(map(int, input().strip().split('.'))))

for cur_ip in input_ips:
    for i in range(4):
        ip[i] &= cur_ip[i]
        min_ip[i] = min(min_ip[i], cur_ip[i])
        max_ip[i] = max(max_ip[i], cur_ip[i])

cnt_lst = []
for i in range(4):
    cnt_lst.append(max_ip[i] - min(min_ip[i], ip[i]))

network_mask = [255, 255, 255, 255]
done = False
for i in range(4):
    if done:
        network_mask[i] = 0
        continue

    if cnt_lst[i] == 0: pass
    else:
        network_mask[i] ^= (2**(len(bin(cnt_lst[i]))-2) - 1)
        done = True

for i in range(4):
    ip[i] = input_ips[0][i] & network_mask[i]

print(".".join(map(str, ip)))
print(".".join(map(str, network_mask)))
