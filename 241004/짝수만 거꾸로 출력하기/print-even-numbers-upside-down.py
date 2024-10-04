n = int(input())
lst = map(int,input().split())
new = []
for s in lst:
    if s % 2 == 0:
        new.append(s)
print(*new[::-1])