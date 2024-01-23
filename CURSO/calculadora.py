n1 = int(input("Ingresa primer numero: "))
n2 = int(input("Ingresa segundo numero: "))

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2}, 
El resultado de la suma es: {suma} 
El resultado de la resta es: {resta}
El resultado de la multiplicacion es: {multiplicacion}  
El resultado de la division es: {division}  
"""
print(mensaje)
