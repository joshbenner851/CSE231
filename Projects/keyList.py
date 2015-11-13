a = {1:2,3:"aaa"}
b = []
print(a.keys())
print(a.values())

for values in a.keys():
    b.append([values,a[values]])

print(b)
