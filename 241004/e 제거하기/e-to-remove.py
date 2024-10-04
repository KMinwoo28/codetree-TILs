n = input()
idx = 0
while True:
    if n[idx] == 'e':
        n = n[:idx] + n[idx + 1:]
        break
    idx += 1
print(n)