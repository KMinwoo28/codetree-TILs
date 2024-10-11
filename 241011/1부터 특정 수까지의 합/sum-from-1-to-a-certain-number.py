n = int(input())
def rem(num):
    s = 0
    for i in range(1, num+1):
        s += i
    return s //10

print(rem(n))