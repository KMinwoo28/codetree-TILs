a, b = map(int,input().split())

mul = [2,4,6,8]

for k in range(4):
    for i in range(b,a-1, -1):
        if i == a:
            print(f"{i} * {mul[k]} = {i * mul[k]}", end = "")
        else:
            print(f"{i} * {mul[k]} = {i * mul[k]} / ", end = "")
    print()