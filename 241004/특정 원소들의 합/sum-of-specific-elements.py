lst = []
for i in range(4):
    lst.append(list(map(int,input().split())))

s = 0
for i in range(4):
    s += sum(lst[i][:i+1])
print(s)