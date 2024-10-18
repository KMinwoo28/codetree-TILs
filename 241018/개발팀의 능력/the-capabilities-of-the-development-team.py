lst = list(map(int,input().split()))

def diff(i,j,k,l):
    sum1 = lst[i] + lst[j]
    sum2 = lst[k] + lst[l]
    sum3 = sum(lst) - sum1 - sum2
    if sum1 != sum2 and sum2 != sum3 and sum3 != sum1:
        return max(sum1, sum2, sum3) - min(sum1, sum2, sum3)
    else:
        return 20000
m = 20000
for i in range(5):
    for j in range(1,5):
        for k in range(5):
            for l in range(1,5):
                if k != i and k != j and l != i and l != j:
                    s = diff(i,j,k,l)
                    m = min(m, s)
if m == 20000:
    print(-1)
else:
    print(m)