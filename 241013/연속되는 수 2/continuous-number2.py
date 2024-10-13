n = int(input())
lst = []
cntlst = []
cnt = 0
for i in range(n):
    lst.append(int(input()))
    if i == 0 or lst[i] != lst[i-1]:
        cntlst.append(cnt)
        cnt = 1
    else:
        cnt += 1
print(max(cntlst))