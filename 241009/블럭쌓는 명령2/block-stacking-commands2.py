N, K = map(int,input().split())
lst = [0]*N
for _ in range(K):
    a, b = map(int,input().split())
    for i in range(a-1,b):
        lst[i] += 1
print(max(lst))