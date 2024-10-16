s = input()
n = len(s)
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if s[i] == '(' and s[j] == ')':
            cnt += 1
print(cnt)