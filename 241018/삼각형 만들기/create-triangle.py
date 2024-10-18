import sys
INT_MAX = sys.maxsize

N = int(input())
lst = [tuple(map(int,input().split())) for _ in range(N)]

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * y2 + x2 * y3 + x3 * y1) -
               (x2 * y1 + x3 * y2 + x1 * y3))
a = - INT_MAX
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1, N):
            x1, y1 = lst[i]
            x2, y2 = lst[j]
            x3, y3 = lst[k]
            if (x1 == x2 or x1 == x3 or x2 == x3) and \
                (y1 == y2 or y1 == y3 or y2 == y3):
                a = max(a, area(x1, y1, x2, y2, x3, y3))
print(a)