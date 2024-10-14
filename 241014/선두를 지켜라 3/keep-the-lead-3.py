a, b = 0, 0
state = 0 # -1 : A가 앞섬, 0 : Tie, 1 : B가 앞섬
before = 0
ainfo = []
binfo = []
N, M = map(int, input().split())
for i in range(N):
    v, t = map(int,input().split())
    for _ in range(t):
        ainfo.append(v)
for i in range(M):
    v, t = map(int,input().split())
    for _ in range(t):
        binfo.append(v)

cnt = 0

for i in range(len(ainfo)):
    a += ainfo[i]
    b += binfo[i]
    
    if state == 0:
        if a < b: # b가 앞선다.
            if before == 0:
                state = 1
                cnt += 1
                before = 1
            elif before == -1:
                state = 1
                cnt += 1
                before = -1
        elif a > b:
            if before == 0:
                state = -1
                cnt += 1
                before = -1
            elif before == 1:
                state = -1
                cnt += 1
                before = -1
    elif state == 1:
        if a > b:
            state = -1
            cnt += 1
            before = -1
        elif a == b:
            state = 0
            cnt += 1
    elif state == -1:
        if a < b:
            state = 1
            cnt += 1
            before = 1
        elif a == b:
            state = 0
            cnt += 1
print(cnt)