n, m = map(int,input().split())
A = list(map(int,input().split()))

def partsum(a1, a2):
    s = 0
    for i in range(a1 - 1, a2):
        s += A[i]
    return s

for _ in range(m):
    a1, a2 = map(int,input().split())
    print(partsum(a1, a2))