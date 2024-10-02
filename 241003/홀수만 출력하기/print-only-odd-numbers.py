N = int(input())
a = []
for _ in range(N):
    t = int(input())
    if t % 3 == 0:
        a.append(t)
for i in a:
    print(i)