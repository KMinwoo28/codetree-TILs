n, t = map(int,input().split())
lst = list(map(int,input().split()))
cntlst = []
cnt = 0
for i in range(n):
    if lst[i] <= t:
        if cnt != 0:
            cntlst.append(cnt)
        cnt = 0
    else:
        cnt += 1
if len(cntlst) != 0:    
    print(max(cntlst))
else:
    print(0)