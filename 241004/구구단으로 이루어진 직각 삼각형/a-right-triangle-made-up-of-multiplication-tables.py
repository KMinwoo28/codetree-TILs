n = int(input())
for i in range(n, 0, -1):
    for j in range(i):
        if j == i - 1:
            print(f"{n - i + 1} * {j + 1} = {(n - i + 1) * (j + 1)}" , end = "")
        else:
            print(f"{n - i + 1} * {j + 1} = {(n - i + 1) * (j + 1)}" , end = " / ")
    print()