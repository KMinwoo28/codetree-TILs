def nstar(n):
    if n == 0:
        return
    print('* '*n)
    nstar(n - 1)
    print('* '*n)

N = int(input())
nstar(N)