lst = list(map(int,input().split()))

def diff(i,j,k,l):
    sum1 = lst[i] + lst[j]
    sum2 = lst[j] + lst[k]
    sum3 = sum(lst) - sum1 - sum2
    rst = abs(sum3 - sum2)
    rst = max(rst, abs(sum3 - sum1))
    rst = max(rst, abs(sum2 - sum1))
    if sum1 != sum2 and sum2 != sum3:
        return True, rst
    else:
        return False, rst
m = 20000
for i in range(5):
    for j in range(1,5):
        for k in range(5):
            for l in range(1,5):
                if k == i or k == j or l == i or l == j:
                    continue
                av, s = diff(i,j,k,l)
                if av:
                    m = min(m,s)
if m != 20000:
    print(m)
else:
    print(-1)