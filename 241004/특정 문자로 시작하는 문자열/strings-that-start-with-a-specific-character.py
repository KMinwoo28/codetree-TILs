n = int(input())
lst = []
for _ in range(n):
    lst.append(input())
target = input()

lenlist = []
for s in lst:
    if s[0] == target:
        lenlist.append(len(s))

avg = sum(lenlist) / len(lenlist)

print(len(lenlist), end = " ")
print("%.2f" %avg )