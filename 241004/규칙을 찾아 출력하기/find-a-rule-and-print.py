n = int(input())

print("* "*n)
for i in range(1,n):
    print("* "*i + "  "*(n-1-i) + "*")