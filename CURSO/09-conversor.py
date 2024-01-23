Variable1 = float(input("Ingrese temperatura a convertir:"))
Varaible2 = input("Es Fahrenheit(F) o Celsius(C)?:")
if Varaible2 == "F" or Varaible2 == "f":
    print((Variable1 - 32) * (5/9))
elif Varaible2 == "C" or Varaible2 == "c":
    print((Variable1 * (9/5)) + 32)
else:
    print("Escala Incorrecta")

