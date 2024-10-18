import sys
INT_MIN = -sys.maxsize
binary = list(map(int,list(input())))
ans = INT_MIN

for i in range(len(binary)):
    binary[i] = 1 - binary[i]

    num = 0
    for j in range(len(binary)):
        num = num * 2 + binary[j]
    ans = max(ans, num)

    binary[i] = 1 - binary[i]
print(ans)