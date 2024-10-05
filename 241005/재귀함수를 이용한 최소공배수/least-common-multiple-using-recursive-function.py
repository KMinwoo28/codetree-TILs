def gcd(a, b):
    while b>0:
        a, b = b, a % b
    return a

def lcd(a, b):
    return (a * b) // gcd(a,b)

n = int(input())
lst = list(map(int,input().split()))
if n == 1:
    print(lst[0])
else:
    s = 1
    for i in range(n):
        s = lcd(s, lst[i])
    print(s)