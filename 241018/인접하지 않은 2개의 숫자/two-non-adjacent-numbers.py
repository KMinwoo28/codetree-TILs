import sys
INT_MIN = - sys.maxsize
n = int(input())
lst = list(map(int,input().split()))
m = INT_MIN
for i in range(n-2):
    for j in range(i+2, n):
        m = max(m, lst[i]+lst[j])
print(m)