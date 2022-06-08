# cities = ["torino","milano","napoli","firenze","bologna"]

# persone = ['luca','giovanni','matteo','paolo']

# elenco = ['sergej','antonov','malik','stanley']

# z = list(("pippo","enzo"))

# print(elenco[0:3])
# print(len(persone))
# print(len(cities))

# print(z)

# print(cities[2:])

# cities.append("catania")
# cities.insert(3, "palermo")
# cities.extend(persone)
# cities[1:-1] = ["boston"]
# print(cities)

# for i in range(len(persone)):
#     print(persone[i])
# print("-----")
# i = -1
# while i < len(persone):
#     print(persone[i])
#     i += 1


# [print(nomi) for nomi in elenco if nomi != "stanley"]

x = ['primo','secondo','terzo']
print(x)

y = x
print(y)
y.append('qaurto')
print(y)
print(x)

z = ("napoli","roma")
zed = list(z)

if "roma" in z:
    print("ok trovato!")
    print(zed)


elenco_citta = ("torino","milano","roma","venezia","firenze","torino")

(x, y, *z) = elenco_citta

print(x)
print(y)
print(z)


for citta in elenco_citta:
    print(citta)


for i in range(len(elenco_citta)):
    print(elenco_citta[i])


i = 0 
while i < len(elenco_citta):
    print(elenco_citta)
    i += 1


x = elenco_citta.index("torino")
print(x)


