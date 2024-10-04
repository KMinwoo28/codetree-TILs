n, m = map(int,input().split())
lst = []
for i in range(n):
    lst.append([0]*n)

for i in range(m):
    a, b = map(int,input().split())
    lst[a-1][b-1] = a*b

for i in range(n):
    print(*lst[i])