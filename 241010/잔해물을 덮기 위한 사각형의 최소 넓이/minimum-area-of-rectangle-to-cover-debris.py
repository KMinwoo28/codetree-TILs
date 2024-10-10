offset = 1000
MAX_R = 2000
lst = [[0] for i in range(offset*2) for j in range(offset*2)]
x1, y1, x2, y2 = map(int,input().split())
for i in range(x1, x2):
    for j in range(y1, y2):
        lst[i+offset][j+offset] = 1

x1, y1, x2, y2 = map(int,input().split())
for i in range(x1, x2):
    for j in range(y1, y2):
        lst[i+offset][j+offset] = 0

min_x, max_x, min_y, max_y = MAX_R, 0, MAX_R, 0

first_rect_exist = False
for x in range(MAX_R):
    for y in range(MAX_R):
        if lst[x][y] == 1:
            first_rect_exist = True
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

if not first_rect_exist:
    area = 0
else:
    area = (max_x - min_x + 1) * (max_y - min_y + 1)

print(area)