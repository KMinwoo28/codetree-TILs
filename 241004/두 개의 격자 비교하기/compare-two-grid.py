n, m = map(int, input().split())
lst1 = []
lst2 = []

for i in range(n):
    lst1.append(list(map(int,input().split())))
for i in range(n):
    lst2.append(list(map(int,input().split())))

new = []
for i in range(n):
    tm = []
    for j in range(m):
        if lst1[i][j] == lst2[i][j]:
            tm.append(0)
        else:
            tm.append(1)
    new.append(tm)

for i in range(n):
    print(*new[i])