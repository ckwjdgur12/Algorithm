import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

N = int(input())

alp_value = {}
for _ in range(N):
    string = list(map(str, input().strip()))

    for i in range(len(string), 0, -1):
        if string[-i] not in alp_value:
            alp_value[string[-i]] = 0
        alp_value[string[-i]] += 10 ** (i-1)

alp_lst = []
for key in alp_value:
    alp_lst.append((alp_value[key], key))

alp_lst.sort(reverse = True)

ans = 0
num = 9
for i in range(len(alp_lst)):
    ans += (alp_lst[i][0] * num)
    num -= 1

print(ans)
