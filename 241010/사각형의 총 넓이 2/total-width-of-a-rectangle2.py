offset = 100
N = int(input())
lst = [[0 for j in range(200)] for i in range(200)]
for _ in range(N):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            lst[i+100][j+100] = 1
cnt = 0
for c in range(200):
    for l in range(200):
        if lst[c][l] == 1:
            cnt += 1
print(cnt)