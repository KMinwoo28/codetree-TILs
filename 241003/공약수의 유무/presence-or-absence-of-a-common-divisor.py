a, b = map(int,input().split())
s = []
for i in range(a, b+1):
    if 1920 % i == 0 and 2880 % i == 0:
        s.append(i)
if len(s) != 0:
    print(1)
else:
    print(0)