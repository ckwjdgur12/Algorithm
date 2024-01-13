import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")


ON = 0
OFF = 1
VAL = 0
LOG = 1


def dfs(v, pre, state):
    if dp[v][state][VAL]: return dp[v][state]

    if state == ON:
        dp[v][ON][VAL] += w[v]
        dp[v][ON][LOG].append(v)
        for n_v in tree[v]:
            if n_v == pre: continue

            n_val, n_log = dfs(n_v, v, OFF)
            dp[v][ON][VAL] += n_val
            dp[v][ON][LOG].extend(n_log)
    else:
        for n_v in tree[v]:
            if n_v == pre: continue

            on_val, on_log = dfs(n_v, v, ON)
            off_val, off_log = dfs(n_v, v, OFF)

            if on_val > off_val:
                dp[v][OFF][VAL] += on_val
                dp[v][OFF][LOG].extend(on_log)
            else:
                dp[v][OFF][VAL] += off_val
                dp[v][OFF][LOG].extend(off_log)

    return dp[v][state]


n = int(input())
w = list(map(int, input().split()))
w.insert(0, 0)
tree = list([] for _ in range(n+1))

for _ in range(n-1):
    fr, to = map(int, input().split())
    tree[fr].append(to)
    tree[to].append(fr)

dp = list(list([0, []] for _ in range(2)) for _ in range(n+1))

on_val, on_log = dfs(1, 0, ON)
off_val, off_log = dfs(1, 0, OFF)

if on_val > off_val:
    print(on_val)
    print(*sorted(on_log))
else:
    print(off_val)
    print(sorted(*off_log))


'''

dp를 써야하는 이유를 먼저 생각하고 접근하자.
이번 같은 경우는 안써도 잘 풀리는 문제.
트리이기 때문에 다시 들어갈 일이 없다.
나는 OFF일때 다시 dfs를 들어가며 쓰이긴 쓰인다.
하지만 이걸 몰랐을때도 무작정 dp를 사용했다.
ON과 OFF값을 모두 한꺼번에 관리한다면 dp를 사용하지 않고도 충분히 풀린다.

문제를 먼저 잘 분석하고 접근하자!

'''
