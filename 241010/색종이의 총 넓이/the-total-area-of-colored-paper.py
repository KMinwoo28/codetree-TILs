offset = 100
n = int(input())
lst = [[0 for j in range(offset*2)] for i in range(offset*2)]
for _ in range(n):
    x1, y1= map(int,input().split())
    for i in range(x1, x1+8):
        for j in range(y1, y1+8):
            lst[i+offset][j+offset] = 1

cnt = 0
for c in range(offset*2):
    for l in range(offset*2):
        if lst[c][l] == 1:
            cnt += 1
print(cnt)