N, M = map(int,input().split())
a, b = 0, 0
moveA = []
moveB = []
for i in range(N):
    m, t = input().split()
    if m == "R":
        for _ in range(int(t)):
            moveA.append(1)
    else:
        for _ in range(int(t)):
            moveA.append(-1)

for i in range(M):
    m, t = input().split()
    if m == "R":
        for _ in range(int(t)):
            moveB.append(1)
    else:
        for _ in range(int(t)):
            moveB.append(-1)


for i in range(max(len(moveA),len(moveB))):
    if i <= len(moveA) - 1:
        a += moveA[i]
    if i <= len(moveB) - 1:
        b += moveB[i]
    if a == b:
        print(i+1)
        break
else:
    print(-1)