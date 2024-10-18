def get_diff(lst, i, j, k):
    sum1 = lst[i] + lst[j] + lst[k]
    sum2 = sum(lst) - sum1
    return abs(sum1 - sum2)
lst = list(map(int,input().split()))
m = 1000000
for i in range(6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            m = min(m, get_diff(lst,i,j,k))
print(m)