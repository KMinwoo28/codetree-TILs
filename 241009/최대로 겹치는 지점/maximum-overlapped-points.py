n = int(input())
lst = [0] * 100
for i in range(n):
    x1, x2 = map(int,input().split())
    if x2 == 100:
        x2 -= 1
    for s in range(x1, x2+1):
        lst[s] += 1
print(max(lst))