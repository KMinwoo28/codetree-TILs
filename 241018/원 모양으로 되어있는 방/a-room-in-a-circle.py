import sys
INT_MAX = sys.maxsize
N = int(input())
lst = [int(input()) for _ in range(N)]
m = INT_MAX
for i in range(N):
    s = 0
    t = 0
    for j in range(i, i + N):
        s += (lst[j%N] * (t))
        t += 1
    m = min(s, m)
print(m)