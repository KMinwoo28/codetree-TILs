dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
direction = {
    "R" : 0,
    "D" : 1,
    "L" : 2,
    "U" : 3
}

def in_x_range(x, n):
    return 0 <= x and x < n 
def in_y_range(y, n):
    return 0 <= y and y < n

n, t = map(int,input().split())
r, c, d = input().split()
r = int(r)
c = int(c)
for i in range(t):
    nx, ny = r + dx[direction[d]], c + dy[direction[d]]
    if not in_x_range(nx, n):
        if d == 'L':
            d == 'R'
        elif d == 'R':
            d == 'L'
    elif not in_y_range(ny, n):
        if d == 'D':
            d == 'U'
        elif d == 'U':
            d == 'D'
    else:
        r, c = r + dx[direction[d]], c + dy[direction[d]]
print(r+1, c+1)