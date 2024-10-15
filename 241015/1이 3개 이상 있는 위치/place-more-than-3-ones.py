dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]


def in_range(x, y, n):
    return 0 <= x and x < n and 0 <= y and y < n

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
validcount = 0
cnt = 0
for x in range(n):
    for y in range(n):    
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny, n) and a[nx][ny] == 1:
                cnt += 1
    if cnt >= 3:
        validcount += 1
print(validcount)