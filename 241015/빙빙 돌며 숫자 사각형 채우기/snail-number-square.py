dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# R, D, L, U
x, y = 0, 0
cur_num = 0
n, m = map(int,input().split())
ans = [
    [0] * m
    for i in range(n)
]

def in_range(x, y):
    return 0<= x and x<n and 0 <= y and y < m
ans[x][y] = 1

for i in range(2,n*m+1):
    nx, ny = x + dx[cur_num], y + dy[cur_num]

    if not in_range(nx, ny) or ans[nx][ny] != 0:
        cur_num = (cur_num + 1) % 4
    x, y = x + dx[cur_num], y + dy[cur_num]
    ans[x][y] = i

for i in range(n):
    for j in range(m):
        print(ans[i][j], end = " ")
    print()