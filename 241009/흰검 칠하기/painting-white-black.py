lst = [[0 for j in range(3)] for i in range(100000)] # W, B
index = 50000
n = int(input())
for i in range(n):
    x, order = input().split()
    x = int(x)
    #print(f'move {index} to', end = " ")
    if order == 'R':
        for s in range(index, index + x):
            lst[s][1] += 1
            lst[s][2] = 1 # set to black
        index += x
    elif order == 'L':
        for s in range(index-1, index - x-1, -1):
            lst[s][0] += 1
            lst[s][2] = 0 # set to white
        index -= x
    #print(lst[index - 7:index+7])
cnt_w = 0
cnt_b = 0
cnt_g = 0
for i in range(100000):
    if (lst[i][0] + lst[i][1]) >= 1:
        # grey decision
        if lst[i][0] >= 2 and lst[i][1] >=2:
            cnt_g += 1
        else:
        # W or B decision
            if lst[i][2] == 0:
                cnt_w += 1
            elif lst[i][2] == 1:
                cnt_b += 1
print(cnt_w,cnt_b,cnt_g)