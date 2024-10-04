n = int(input())
lst = [int(input()) for i in range(n)]
s = str(sum(lst))
print(s[1:] + s[:1])