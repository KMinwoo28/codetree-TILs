n = int(input())
s = input().replace(" ", '')
t = len(s) // 5
i = 0

for _ in range(t):
    print(s[i:i+5])
    i += 5
print(s[i:])