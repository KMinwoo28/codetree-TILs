A = input()
B = input()

for i in range(1, 1 + len(A)):
    B = B[1:] + B[0]
    if A == B:
        print(i)
        break
else:
    print(-1)