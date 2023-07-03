import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    global ans
    dq = deque()
    dq.append((x, y))
    v = [[False] * w for _ in range(h)]

    while dq:
        x, y = dq.popleft()
        v[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < h and 0 <= ny < w and not v[nx][ny]): continue    # 범위를 넘어가면 돌어감
            if bldg[nx][ny] == '*': continue    # 벽을 만나면 돌아감
            if bldg[nx][ny].isalpha() and bldg[nx][ny].isupper() and bldg[nx][ny] not in key: continue  # 열쇠가 없는 문을 만나면 돌어감
            if bldg[nx][ny].isalpha() and bldg[nx][ny].islower() and bldg[nx][ny].upper() not in key:   # 열쇠를 얻었을경우 추가하고 다시 시작
                key.append(bldg[nx][ny].upper())
                for i in range(w):
                    if bldg[0][i] == bldg[nx][ny].upper(): 
                        startPoint.append((0, i))
                    if bldg[h-1][i] == bldg[nx][ny].upper(): 
                        startPoint.append((h-1, i))
                for i in range(1, h-1):
                    if bldg[i][0] == bldg[nx][ny].upper(): 
                        startPoint.append((i, 0))
                    if bldg[i][w-1] == bldg[nx][ny].upper(): 
                        startPoint.append((i, w-1))
                return True
            
            if bldg[nx][ny] == '$' and not isChecked[nx][ny]:   # 처음 본 문서를 만나면 확인표시 후 ans 1 증가
                ans += 1
                isChecked[nx][ny] = True

            v[nx][ny] = True
            dq.append((nx, ny))

    return False


for _ in range(int(input())):
    specialCase = 0
    h, w = map(int, input().split())

    bldg = []
    for _ in range(h):
        bldg.append(list(input().strip()))  # bldg 정보 입력

    key = []
    inputKey = input().strip()
    inputKey = inputKey.upper()
    if inputKey != '0':
        for alp in inputKey:
            key.append(alp) # 주어진 Key 넣기

    startPoint = []
    specialPos = []
    for i in range(w):  # 첫행, 마지막 행의 시작점 확인
        if bldg[0][i] == '.' or bldg[0][i] in key: startPoint.append((0, i))
        if bldg[h-1][i] == '.' or bldg[h-1][i] in key: startPoint.append((h-1, i))
        
        if bldg[0][i].islower():    # lowerCase, 즉 Key인 경우 Key에도 추가
            key.append(bldg[0][i].upper())
            startPoint.append((0, i))
        if bldg[h-1][i].islower():
            key.append(bldg[h-1][i].upper())
            startPoint.append((h-1, i))
        
        if bldg[0][i] == '$':   # $, 즉 문서인 경우 Key에도 추가
            specialCase += 1
            startPoint.append((0, i))
            specialPos.append((0, i))   # 중복 방지를 위해 따로 저장
        if bldg[h-1][i] == '$':
            specialCase += 1
            startPoint.append((h-1, i))
            specialPos.append((h-1, i)) # 중복 방지를 위해 따로 저장

    for i in range(1, h-1): # 첫열, 마지막 열의 시작점 확인
        if bldg[i][0] == '.' or bldg[i][0] in key: startPoint.append((i, 0))
        if bldg[i][w-1] == '.' or bldg[i][w-1] in key: startPoint.append((i, w-1))
        
        if bldg[i][0].islower():    # lowerCase, 즉 Key인 경우 Key에도 추가
            key.append(bldg[i][0].upper())
            startPoint.append((i, 0))
        if bldg[i][w-1].islower(): 
            key.append(bldg[i][w-1].upper())
            startPoint.append((i, w-1))

        if bldg[i][0] == '$':   # $, 즉 문서인 경우 Key에도 추가
            specialCase += 1
            startPoint.append((i, 0))
            specialPos.append((i, 0))   # 중복 방지를 위해 따로 저장
        if bldg[i][w-1] == '$': 
            specialCase += 1
            startPoint.append((i, w-1))
            specialPos.append((i, w-1)) # 중복 방지를 위해 따로 저장

    while True:
        keyAppended = False
        startAgain = False
        isChecked = [[False] * w for _ in range(h)] # 획득한 문서인지 확인
        for x, y in specialPos:
            isChecked[x][y] = True # 중복 방지를 위해 미리 저장해둔 위치 표시

        ans = 0
        for x, y in startPoint:
            keyAppended = bfs(x, y)
            if keyAppended: # 새로운 Key가 추가되었다면 처음부터 다시 실행
                startAgain = True
                break
        if startAgain: continue
        break

    print(ans + specialCase)


    
'''

1
7 7
*ABCDE$
X.....F
W.$$$.G
*.$$$.$
U.$$$.J
T.....K
*SQPML*
irony

1
10 17
*****************
.............**$*
*B*A*P*C**X*Y*.X.
*y*x*a*p**$*$**$*
*******b*********
*******B**$$$****
B$*****$**r*Q**$B
**********R*q****
*$APCZ$$$$$*q**$A
************q****
cz

1
3 5
*****
.b*$B
*****
a

1
5 9
*********
.......a*
***.*****
*$Ab*****
*********
0

1
5 5
aa*aa
a*A*a
*A$A*
a*A*a
aa*aa
0

2
5 7
*******
*******
*******
**$....
*******
0
5 4
****
**$.
****
****
****
0

0
0
4
3
1
1
0
0
2
1
12
10000
0
0

'''    