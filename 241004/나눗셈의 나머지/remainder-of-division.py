a, b = map(int,input().split())

rem = [0] * b
while a > 1:
    rem[a % b] += 1
    a = a // b

sum = 0
for r in rem:
    sum += r**2
print(sum)