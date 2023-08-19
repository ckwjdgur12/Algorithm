import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def make_strings():
    strings.append("()")

    for i in range(4, len(S)+1, 2):
        for s in strings:
            if (i-2) % len(s) != 0: continue
            tmp_str = "("
            tmp_str += s * ((i-2) // len(s))
            tmp_str += ")"
            strings.append(tmp_str)
    
    strings.sort()
    return


def find_string(k):
    for s in strings:
        idx = 0
        for i in range(len(S)):
            if s[idx] == S[i]: idx += 1
            if idx == len(s): break

        if idx == len(s):
            k -= 1
            if k == 0: return s

    return -1


S = list(input().strip())
K = int(input())

strings = []

make_strings()

ans = find_string(K)

print(ans)


'''

d = ()

len = 4
d = (), (())

len = 6
d = (), (()), (()()), ((()))

len = 8
d = (), (()), (()()), ((())), (()()()), ((()())), (((())))

len = 10
d = (), (()), (()()), ((())), (()()()), ((()())), (((()))), 
(()()()()), ((())(())), ((()()())), (((()()))), ((((()))))


'''


'''

d = ["()", "(())", "(()())", "((()))", "(()()())", "((()()))", "(((())))", 
"(()()()())", "((())(()))", "((()()()))", "(((()())))", "((((()))))"]

print(d)
d.sort()
print(d)

'''
