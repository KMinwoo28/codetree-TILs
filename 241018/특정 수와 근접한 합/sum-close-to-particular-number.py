import sys
INT_MAX = sys.maxsize
N, S = map(int,input().split())
lst = list(map(int,input().split()))
m = INT_MAX
for i in range(N-1):
    for j in range(i,N):
        ext = lst[:i] + lst[i+1:j] + lst[j+1:]
        m = min(m, abs(S - sum(ext)))
print(m)