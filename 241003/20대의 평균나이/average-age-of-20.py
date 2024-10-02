a = []
while True:
    age = int(input())
    if age <30:
        a.append(age)
    elif age >= 30:
        break
res = float(round(sum(a)/len(a), 2))
print("%.2f" %res)