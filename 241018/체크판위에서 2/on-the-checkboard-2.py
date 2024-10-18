n, m = map(int,input().split())
lst = []
for i in range(n):
    lst.append(list(input().split()))

cnt = 0
for i in range(1, n):
    for j in range(1, m):
        for k in range(i+1, n - 1):
            for l in range(j + 1, m - 1):
                if lst[0][0] != lst[i][j] and \
                   lst[i][j] != lst[k][l] and \
                   lst[k][l] != lst[n-1][m-1]:
                    cnt += 1
print(cnt)