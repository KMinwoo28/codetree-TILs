def hap(n):
    if n == 1:
        return 1
    return n + hap(n - 1)
N = int(input())
print(hap(N))