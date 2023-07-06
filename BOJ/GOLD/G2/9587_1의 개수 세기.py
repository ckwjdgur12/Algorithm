import sys
input = sys.stdin.readline
# sys.stdin = open("BOJ/input.txt", "r")

def check(num):
    cnt = 0
    bin_num = bin(num)[2:] # 앞에 0, 1 index에 있는 0b 빼줌
    length = len(bin_num)

    for i in range(length):
        if bin_num[i] == '1':
            power = length - i - 1
            cnt += powerSum[power]
            cnt += (num + 1 - 2**power)
            num = num - 2**power
    
    return cnt



A, B = map(int, input().split())

powerSum = [0] * 61
for i in range(1, 60):
    powerSum[i] = 2**(i-1) + 2 * powerSum[i-1]

print(check(B) - check(A-1))
