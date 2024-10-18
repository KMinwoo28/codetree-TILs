import sys
INT_MAX = sys.maxsize

N = int(input())
lst = []
for i in range(N):
    lst.append(tuple(map(int,input().split())))

m = INT_MAX
for i in range(1, N - 1):
    s= 0 
    ext = lst[:i]+lst[i+1:]
    
    for j in range(1, len(ext)):
        s += (abs(ext[j][0] - ext[j-1][0]) + abs(ext[j][1] - ext[j-1][1]))
    
    m = min(m, s)
print(m)