import sys
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

N = int(input())
dots = [tuple(map(int,input().split())) for _ in range(N)]
area = INT_MAX
for i in range(N):
    maxx, minx, maxy, miny = INT_MIN, INT_MAX, INT_MIN, INT_MAX
    for j in range(N):
        if i == j:
            continue
        maxx, minx, maxy, miny = max(maxx, dots[j][0]), min(minx, dots[j][0]),\
                                 max(maxy, dots[j][1]), min(miny, dots[j][1])
    a = (maxx-minx)*(maxy-miny)
    area = min(area, a)
print(area)