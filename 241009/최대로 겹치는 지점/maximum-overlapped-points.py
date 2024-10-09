n = int(input())
lst = [0] * 100
for i in range(n):
    x1, x2 = map(int,input().split())
    for s in range(x1, x2+2):
        lst[s] += 1
print(max(lst))