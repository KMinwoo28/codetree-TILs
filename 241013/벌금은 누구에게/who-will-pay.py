N, M, K = map(int,input().split())
war = [0 for i in range(N)]
for i in range(M):
    s = int(input())
    war[s-1] += 1
    if war[s-1] >= K:
        print(s)
        break
else:
    print(-1)