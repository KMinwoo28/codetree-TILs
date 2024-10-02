N = int(input())
a = []
for _ in range(N):
    t = int(input())
    if t % 3 == 0 and t % 2 == 1:
        a.append(t)
for i in a:
    print(i)