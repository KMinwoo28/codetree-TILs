n = int(input())
lst = list(map(int,input().split()))
m = 101
for i in range(n):
    for j in range(i+1, n):
        if abs(lst[i] - lst[j]) < m:
            m = abs(lst[i] - lst[j])

print(m)