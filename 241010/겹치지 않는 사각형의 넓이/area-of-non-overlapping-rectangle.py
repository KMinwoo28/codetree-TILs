offset = 1000

lst = [[0 for j in range(2000)] for i in range(2000)]
for _ in range(2):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            lst[i+offset][j+offset] = 1
x1, y1, x2, y2 = map(int,input().split())
for i in range(x1, x2):
    for j in range(y1, y2):
        lst[i+offset][j+offset] = 0

cnt = 0
for c in range(2000):
    for l in range(2000):
        if lst[c][l] == 1:
            cnt += 1
print(cnt)