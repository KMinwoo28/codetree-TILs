N, M = map(int,input().split())
a, b = 0, 0
moveA = []
moveB = []
for i in range(N):
    t, d = input().split()
    if d == "R":
        for _ in range(int(t)):
            moveA.append(1)
    else:
        for _ in range(int(t)):
            moveA.append(-1)

for i in range(M):
    t, d = input().split()
    if d == "R":
        for _ in range(int(t)):
            moveB.append(1)
    else:
        for _ in range(int(t)):
            moveB.append(-1)


same = 0 # 현재 같은 위치 : 0, 다름 : 1
cnt = 0

for i in range(max(len(moveA),len(moveB))):
    if i <= len(moveA) - 1:
        a += moveA[i]
    if i <= len(moveB) - 1:
        b += moveB[i]
    if a == b:
        if same != 0:
            cnt += 1
            same = 0
    elif a < b:
        if same == 0:
            same = 1
    elif a > b:
        if same == 0:
            same = 1
print(cnt)