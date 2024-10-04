N = int(input())
for i in range(1, 1 + N):
    for j in range(N - i + 1, N + 1):
        print(j, end = " ")
    print()