n = int(input())
temp = 0
lst = [0] * 1000
index = 500
for i in range(n):
    x, order = input().split()
    x = int(x)
    
    if order == 'R':
        for s in range(index, index + x):
            lst[s] += 1        
        index += x
    elif order == 'L':
        for s in range(index, index - x , -1):
            lst[s] += 1
        index -= x
cnt = 0
for i in range(len(lst)):
    if lst[i] >= 2:
        cnt += 1
print(cnt)