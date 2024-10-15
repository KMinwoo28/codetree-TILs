dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# R, D, L, U

cur_num = 2
n = int(input())
ans = [
    [0] * n
    for i in range(n)
]
x, y = n-1, n-1
def in_range(x, y):
    return 0<= x and x<n and 0 <= y and y < n
ans[x][y] = n**2

for i in range(2,n*n+1):
    nx, ny = x + dx[cur_num], y + dy[cur_num]
    if not in_range(nx, ny) or ans[nx][ny] != 0:
        cur_num = (cur_num + 1) % 4
    x, y = x + dx[cur_num], y + dy[cur_num]
    ans[x][y] = n**2 - i + 1

for i in range(n):
    for j in range(n):
        print(ans[i][j], end = " ")
    print()