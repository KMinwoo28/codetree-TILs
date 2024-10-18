N = int(input())
d1 = list(map(int,input().split()))
d2 = list(map(int,input().split()))

def dec(tar, n):
    if abs(tar - n) <= 2 or abs(tar + N - n) <= 2 or abs(tar - N - n) <= 2:
        return True
    else:
        return False

s = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            if (dec(d1[0], i) and dec(d1[1], j) and dec(d1[2], k)) or \
               (dec(d2[0], i) and dec(d2[1], j) and dec(d2[2], k)):
                s += 1
print(s)