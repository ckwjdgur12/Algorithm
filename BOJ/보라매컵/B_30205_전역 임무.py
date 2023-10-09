import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

N, M, power = map(int, input().split())

bases = list(list(map(int, input().split())) for _ in range(N))

for base in bases:
    item_cnt = base.count(-1)
    base.sort()
    for c_l in base:
        if c_l == -1: continue

        if c_l <= power: power += c_l
        else:
            while item_cnt > 0:
                power *= 2
                item_cnt -= 1
                if c_l <= power: 
                    power += c_l
                    break

            if c_l > power:
                print(0)
                exit(0)

    while item_cnt > 0:
        power *= 2
        item_cnt -= 1

print(1)
