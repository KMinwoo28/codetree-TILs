n = int(input())
for i in range(1, 1+n):
    for j in range(n, 0, -1):
        print(i*j, end = " ")
    print()