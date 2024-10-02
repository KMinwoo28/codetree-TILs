a = []
while True:
    age = int(input())
    if age <30 and age >= 20:
        a.append(age)
    else:
        break
res = round(sum(a)/len(a), 2)
print("%.2f" %res)