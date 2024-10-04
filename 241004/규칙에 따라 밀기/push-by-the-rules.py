n = input()
order = input()
r = order.count('R')
l = order.count('L')
shift = r - l
if shift < 0: # shift to left
    n = n[abs(shift):] + n[:abs(shift)]
elif shift > 0: # shift to right
    n = n[:len(n) - shift] + n[len(n) - shift :]
print(n)