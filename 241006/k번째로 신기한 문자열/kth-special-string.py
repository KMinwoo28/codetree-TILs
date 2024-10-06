n, t, letter = input().split()

lst = []
for i in range(int(n)):
    a = input()
    if letter == a[:len(letter)]:
        lst.append(a)

lst.sort()
print(lst[int(t) - 1])