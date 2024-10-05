def nprint(n):
    if n == 1 or n == 2:
        return n
    return nprint(n//3) + nprint(n-1)

n = int(input())
print(nprint(n))