a, b = map(int,input().split())
n = input()

# n to decimal
s = 0
for i in range(len(n)):
    s += int(n[len(n)-i-1])*(a**i)

# s to b-ary
remainder = []
while s>=b:
    remainder.append(str(s % b))
    s = s // b
remainder.append(str(s))
print(''.join(remainder[::-1]))