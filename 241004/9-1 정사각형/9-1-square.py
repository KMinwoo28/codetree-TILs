cnt = 0
sq = [9,8,7,6,5,4,3,2,1]
n = int(input())

for i in range(n):
    for j in range(n):
        print(sq[cnt], end = "")
        cnt = (cnt + 1) % 9
    print()