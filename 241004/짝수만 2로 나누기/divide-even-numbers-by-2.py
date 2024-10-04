N = int(input())
lst = list(map(int,input().split()))

def div(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] //= 2

div(lst)
print(*lst)