N = int(input())
a, b, c = map(int,input().split())
s = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if abs(i - a) <= 2 or abs(j - b) <= 2 or abs(k - c) <= 2: 
                s += 1
print(s)