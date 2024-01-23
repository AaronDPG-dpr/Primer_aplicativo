# lenguajes =  ["Phyton", "Ruby", "PHP", "Jvascript", "Java"]

# for dd in lenguajes:
#         print(dd)

buscar = 6
for numero in range(5):  # renge(5) es un iterable
    if numero == buscar:
        print("Econtrado", buscar)
        break
else:
    print("No encontrado")

for char in "Ultimate Python":
    print(char)
