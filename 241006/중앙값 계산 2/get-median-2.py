n = int(input())
lst = list(map(int,input().split()))

res = []
for i in range(0,n,2):
    ls = lst[:i+1]
    res.append(sorted(ls)[i//2])
print(*res)