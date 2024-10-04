n = int(input())
for _ in range(n):
    a, b = map(int,input().split())
    if a % 2 == 0:
        E = [s for s in range(a, b+1, 2)] 
    else:
        E = [s for s in range(a+1, b+1, 2)]
    print(sum(E))