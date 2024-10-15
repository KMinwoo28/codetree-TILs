N, M = map(int,input().split())
lst = [[0 for i in range(N)] for j in range(N)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

for i in range(M):
    cnt = 0
    r, c = map(int,input().split())
    lst[r-1][c-1] = 1
    for j in range(4):
        tx, ty = r-1 + dx[j], c-1 + dy[j]
        if in_range(tx, ty) and lst[tx][ty] != 0:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)