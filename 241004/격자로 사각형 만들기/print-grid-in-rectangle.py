lst = []
n = int(input())
for i in range(n):
    lst.append([1]*n)
for i in range(1,n):
    for j in range(1,n):
        lst[i][j] = lst[i][j-1] + lst[i-1][j] + lst[i-1][j-1]

for i in range(n):
    print(*lst[i])