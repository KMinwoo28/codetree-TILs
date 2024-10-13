def sign(num):
    if num < 0:
        return -1
    else:
        return 1
n = int(input())
lst = []
cntlst = []
cnt = 0
for i in range(n):
    lst.append(sign(int(input())))
    if i == 0 or lst[i] != lst[i-1]:
        cntlst.append(cnt)
        cnt = 1
    else:
        cnt += 1
cntlst.append(cnt)
print(max(cntlst))