def nprint(n):
    if n != 1:
        nprint(n - 1)
    print(n, end = " ")
    return

def revprint(n):
    if n == 0:
        return
    print(n, end = " ")
    revprint(n - 1)

N = int(input())
nprint(N)
print()
revprint(N)