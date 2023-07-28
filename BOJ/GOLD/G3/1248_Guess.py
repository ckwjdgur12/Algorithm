import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def back_tracking(depth, seq):

    if depth == n:
        print(*seq)
        exit(0)

    for num in range(-10, 11, 1):
        
        flag = True
        for i in range(depth + 1):
            next_sign = sign_mat[i][depth]
            next_num = sum(seq[i:depth+1]) + num

            if next_sign == '0' and next_num != 0:
                flag = False
                break
            elif next_sign == '+' and next_num <= 0:
                flag = False
                break
            elif next_sign == '-' and next_num >= 0: 
                flag = False
                break

        if flag:
            seq.append(num)
            back_tracking(depth + 1, seq)
            seq.pop()

    return


n = int(input())
string = input().strip()
sign_mat = []

start = 0
for i in range(n, 0, -1):
    tmp_str = [None] * (n-i)

    for elem in string[start:i+start]:
        tmp_str.append(elem)

    sign_mat.append(tmp_str)
    start += i

seq = []
back_tracking(0, seq)
