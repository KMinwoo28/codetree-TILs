def nprint(n):
    if n == 0:
        return
    print(n, end = " ")
    nprint(n- 1)
    print(n, end = " ")

N = int(input())
nprint(N)