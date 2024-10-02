a = []
for i in range(100):
    age = int(input())
    if age <30:
        a.append(age)
    elif age >= 30:
        break
res = round(sum(a)/len(a), 2)
print("%.2f" %res)