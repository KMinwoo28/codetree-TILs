import sys
Minsize = -sys.maxsize
N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int,input().split())))
val = Minsize
for i in range(N):
    for j in range(N-2):
        l = lst[i][j] + lst[i][j+1] + lst[i][j+2]
        val = max(l, val)
print(val)