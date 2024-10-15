dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dire = {
    "E" : 0,
    "S" : 1,
    "W" : 2,
    "N" : 3
}
x, y = 0, 0
N = int(input())
t = 0
Find = False
for i in range(0, N):
    D, r = input().split()
    for s in range(int(r)):
        x , y = x + dx[dire[D]], y + dy[dire[D]]
        t += 1
        if x == 0 and y == 0:
            Find = True
            break
    if Find:
        print(t)
        break
else:
    print(-1)