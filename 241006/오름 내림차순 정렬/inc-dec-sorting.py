n = int(input())
lst = list(map(int,input().split()))

print(*sorted(lst))
print(*sorted(lst, reverse = True))