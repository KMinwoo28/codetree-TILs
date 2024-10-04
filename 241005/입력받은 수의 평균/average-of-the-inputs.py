n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))
avg = sum(s) / len(s)
print("%.1f" %avg)
if avg < 70:
    print('fail')