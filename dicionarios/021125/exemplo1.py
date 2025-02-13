ra = {"Liz": 229874, "Hugo":215793, "Sofia": 199745}
print(type(ra))
print(ra["Liz"])
print(ra["Sofia"])
print(ra)
ra["Hugo"] = 222555
print(ra)

for x in ra:
    print(x)


print("Sofia" in ra)
print("Aline" in ra)

print(ra)

print(ra.items())
print(ra.keys())
print(ra.values())

print(list(ra.items()))
print(list(ra.keys()))
print(list(ra.values()))

print(ra.get("Hugo"))
print(ra.get("Maria"))
print(ra.get("Maria","N/A"))

for nome, numero in ra.items():
    print(nome, numero, sep=' ')