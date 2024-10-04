def gcd(a, b):
    while b>0:
        a, b = b, a % b
    return a

def lcd(a, b):
    return (a * b) // gcd(a,b)

n,m = map(int,input().split())
print(lcd(n,m))