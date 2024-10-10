offset = 100
n = int(input())
lst = [[0 for i in range(offset*2)] for j in range(offset*2)]
for i in range(n):
    x1, y1, x2, y2 = map(int,input().split())
    if i % 2 == 0: # 빨간색
        for c in range(x1, x2):
            for r in range(y1, y2):
                lst[c+offset][r+offset] = 1
    else: # 파란색
        for c in range(x1, x2):
            for r in range(y1, y2):
                lst[c+offset][r+offset] = 2
cnt = 0
for i in range(offset*2):
    for j in range(offset*2):
        if lst[i][j] == 2:
            cnt += 1
print(cnt)