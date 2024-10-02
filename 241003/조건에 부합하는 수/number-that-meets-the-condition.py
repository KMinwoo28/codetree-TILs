a = int(input())
for i in range(1, 1+ a):
    if i % 2 == 1 or i % 4 == 0:
        if (i // 8) % 2 == 1:
            if i % 7 >= 4:
                print(i, end = " ")