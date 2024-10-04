s = []
for _ in range(3):
    m = input()
    s.append(len(m))
s = sorted(s)
print(abs(s[0] - s[-1]))