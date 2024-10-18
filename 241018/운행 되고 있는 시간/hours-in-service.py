N = int(input())
work = [tuple(map(int,input().split())) for _ in range(N)]
m = 0
for i in range(N):
    time = [0] * 1000
    for j in range(N):
        if i == j:
            continue
        for k in range(work[j][0], work[j][1]):
            time[k] = 1
    m = max(sum(time), m)
print(m)