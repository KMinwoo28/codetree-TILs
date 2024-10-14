dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x, y = 0, 0
cur_dir = 3

order = input()
for s in order:
    if s == "L":
        cur_dir = (cur_dir - 1) % 4
    elif s == "R":
        cur_dir = (cur_dir + 1) % 4
    elif s == "F":
        x += dx[cur_dir]
        y += dy[cur_dir]
print(x, y)