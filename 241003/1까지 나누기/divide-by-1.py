n = int(input())
i = 1
while True:
    n = n // i
    if n <= 1:
        break
    i += 1
print(i)