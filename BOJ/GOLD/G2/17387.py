#
# 그냥 수학문제..
#

import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

X1, Y1, X2, Y2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
X3, Y3, X4, Y4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

ccw123 = ccw(x1, y1, x2, y2, x3, y3)
ccw124 = ccw(x1, y1, x2, y2, x4, y4)
ccw341 = ccw(x3, y3, x4, y4, x1, y1)
ccw342 = ccw(x3, y3, x4, y4, x2, y2)

if ccw123*ccw124 == 0 and ccw341*ccw342 == 0:
    if X1 <= X4 and X3 <= X2 and Y1 <= Y4 and Y3 <= Y2:
        print(1); exit(0)
else:
    if ccw123*ccw124 <= 0 and ccw341*ccw342 <= 0:
        print(1); exit(0)

print(0)

