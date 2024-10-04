n = int(input())
lst = []
for i in range(n):
    lst.append([0]*n) 
cnt = 1
for j in range(n-1, -1, -1):
    if j % 2 == 1:
        for i in range(n-1, -1, -1):
            
            lst[i][j] = cnt
            cnt += 1
            
    elif j % 2 == 0:
        for i in range(n):
            
            lst[i][j] = cnt
            cnt += 1
            
    

for i in range(n):
    print(*lst[i])