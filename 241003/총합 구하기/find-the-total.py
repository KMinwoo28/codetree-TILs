a ,b  = map(int,input().split())
s = []
for i in range(a, b+1):
    if i % 6 == 0 and i % 8 != 0:
        s.append(i)
print(sum(s))