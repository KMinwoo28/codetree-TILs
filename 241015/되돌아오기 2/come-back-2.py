# 상, 우, 하, 좌
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0, 0
d = 0
order = input()
for i in range(len(order)):
    o = order[i]
    if o == 'R':
        d = (d + 1)% 4
    elif o == "L":
        d = (d + 3) % 4
    elif o == 'F':
        x, y = x + dx[d], y + dy[d]
        if x == 0 and y == 0:
            print(i + 1)
            break
else:
    print(-1)