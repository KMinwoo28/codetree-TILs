import sys
n = int(input())
people = list(map(int,input().split()))
INT_MAX = sys.maxsize

min_val = INT_MAX

for i in range(n):
    val = 0
    for j in range(n):
        val += people[j]*abs(j - i)
    
    min_val = min(val, min_val)

print(min_val)