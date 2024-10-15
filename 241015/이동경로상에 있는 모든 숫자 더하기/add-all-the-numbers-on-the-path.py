dx, dy = [-1,0, 1, 0], [0,1,0,-1]
# U, R, D, L

n, T = map(int,input().split())
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n
cur_dir = 0

x, y = n//2, n//2
a = []
order = input()
for i in range(n):
    a.append(list(map(int,input().split())))
s = a[x][y]

for i in range(len(order)):
    if order[i] == "R":
        cur_dir = (cur_dir + 1) % 4
    elif order[i] == 'L':
        cur_dir = (cur_dir + 3) % 4
    elif order[i] == 'F':
        nx, ny = x + dx[cur_dir], y + dy[cur_dir]
        if in_range(nx, ny):
            x, y = nx, ny
            s += a[x][y]
print(s)