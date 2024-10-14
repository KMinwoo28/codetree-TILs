dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
# 1: E, 2: S, 3: N, 4: W
move = ['W','S','E','N']
x, y = 0,0
N = int(input())
for _ in range(N):
    D, d = input().split()
    x += dx[move.index(D)]*int(d)
    y += dy[move.index(D)]*int(d)
print(x,y)