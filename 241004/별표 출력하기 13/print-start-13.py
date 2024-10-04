n = int(input())
s = ['']*n

initascend = 1
initdescend = 0
for i in range(0,n,2): # 0,2,4,...
    s[i] = '* ' * (n - initdescend)
    initdescend += 1

for i in range(1,n,2): # 1,3,5,...
    s[i] = '* ' * (initascend)
    initascend += 1

for sym in s:
    print(sym)
for sym in s[::-1]:
    print(sym)