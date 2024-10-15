# R, D, L, U
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

direct = {
    "R" : 0,
    'D' : 1,
    'L' : 2,
    'U' : 3
}
def left_mir(d): # \일때
    if d == 'U':
        return 'L'
    elif d == 'L':
        return 'U'
    elif d == "R":
        return 'D'
    elif d == 'D':
        return 'R'

def right_mir(d): # /일때
    if d == 'U':
        return 'R'
    elif d == 'L':
        return 'U'
    elif d == "R":
        return 'U'
    elif d == 'D':
        return 'L'

N = int(input())
def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

mirror = []
for i in range(N):
    mirror.append(list(input()))

d = 0
# Initialization
K = int(input()) - 1
m, re = K // N, K % 3
r, c = 0, 0
match m:
    case 0:
        r, c = 0, re
        d = 'D'
    case 1:
        r, c = re, N-1
        d = 'L'
    case 2:
        r, c = N-1, 2 - re
        d = 'U'
    case 3:
        r, c = 2 - re, 0
        d = 'R'
cnt = 0
while True:
    cnt += 1
    s = mirror[r][c]
    n_d = left_mir(d) if s == '\\' else right_mir(d)
    nr, nc = r + dx[direct[n_d]], c + dy[direct[n_d]]
    if not in_range(nr, nc):
        break
    r, c = r + dx[direct[n_d]], c + dy[direct[n_d]]
    d = n_d
print(cnt)