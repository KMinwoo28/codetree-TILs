import sys
INT_MAX = sys.maxsize
N, H, T = map(int,input().split())
lst = list(map(int,input().split()))
m = INT_MAX
for i in range(N - T + 1):
    s = 0
    for j in range(i, i+T):
        s += abs(lst[j] - H)
    m = min(m, s)
print(m)