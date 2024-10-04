al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cnt = 0
N = int(input())
for i in range(N):
    for j1 in range(i):
        print("  ", end = "")
    for j2 in range(N - i):
        print(f"{al[cnt]} ", end = "")
        cnt = (cnt + 1) % 26
    print()