n = int(input())
offset = 100
lst = [0] * 201
for i in range(n):
    x1, x2 = map(int,input().split())
    for s in range(x1, x2):
        lst[s+100] += 1
print(max(lst))