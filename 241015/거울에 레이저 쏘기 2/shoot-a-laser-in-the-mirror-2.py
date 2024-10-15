# R, D, L, U
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def left_mir(d): # \일때
    if d == 3:
        return 2
    elif d == 2:
        return 3
    elif d == 0:
        return 1
    elif d == 1:
        return 0

def right_mir(d): # /일때
    if d == 3:
        return 0
    elif d == 2:
        return 1
    elif d == 0:
        return 3
    elif d == 1:
        return 2

N = int(input())
def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

mirror = []
for i in range(N):
    mirror.append(list(input()))

d = 0
# Initialization
K = int(input()) - 1
m, re = K // N, K % N
r, c = 0, 0
match m:
    case 0:
        r, c = 0, re
        d = 1
    case 1:
        r, c = re, N-1
        d = 2
    case 2:
        r, c = N-1, (N-1) - re
        d = 3
    case 3:
        r, c = (N-1) - re, 0
        d = 0
cnt = 0
while True:

    cnt += 1
    s = mirror[r][c]
    n_d = left_mir(d) if s == '\\' else right_mir(d)
    nr, nc = r + dx[n_d], c + dy[n_d]
    if not in_range(nr, nc):
        break
    r, c = r + dx[n_d], c + dy[n_d]
    d = n_d
print(cnt)