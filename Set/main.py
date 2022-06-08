#set

x = {"torino","roma","milano","milano",23}

y = {23, 45, 32, 12, "milano"}

print(len(x))
print(len(y))

for citta in x:
    print(citta)

print("roma" in x)

x.add("toronto")

for citta in x:
    print(citta)

x.intersection(y)

z = x.symmetric_difference(y)

print(z)

for citta in x:
    print(citta)

x.discard("roma")

print(x)

x.union(y)

print(x)