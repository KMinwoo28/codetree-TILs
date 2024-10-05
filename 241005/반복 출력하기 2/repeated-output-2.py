N = int(input())
def Nprint(N):
    if N == 0:
        
        return
    else:
        print('HelloWorld')
        Nprint(N - 1)

Nprint(N)