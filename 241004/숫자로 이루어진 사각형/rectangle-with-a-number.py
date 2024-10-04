def square(n):
    num  = [1,2,3,4,5,6,7,8,9]
    lst = []
    cnt = 0
    for i in range(n):
        col = []
        for j in range(n):
            col.append(num[cnt])
            cnt = (cnt + 1) % 9
        lst.append(col)
    for i in range(n):
        print(*lst[i])

N = int(input())
square(N)