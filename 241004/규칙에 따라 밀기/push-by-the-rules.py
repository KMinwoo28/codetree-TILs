n = input()
order = input()
for i in range(len(order)):
    if order[i] == 'R':
        n = n[-1] + n[:-1]
    elif order[i] == 'L':
        n = n[1:] + n[0]
print(n)