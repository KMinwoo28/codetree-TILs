ls = list(map(int,input().split()))
idx = 0
for i in range(10):
    if ls[i] % 3 == 0:
        idx = i - 1
        break
print(ls[idx])