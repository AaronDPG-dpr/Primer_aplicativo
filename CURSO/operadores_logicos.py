# and, or, not
"""la primera es cuando ambas condiciones se cumplen o son verdaderas
si una es falsa entonces todo es falso"""
"""la segunda es cuando una de las condiciones se cumplen o una es verdadera
para que el resultado sea falso, todas las condiciones tienen que ser falsas"""
# la tercera niega el resultado de una condicion
# la prioridad es del parentesis, luego las de afuera

"""operacion de corto circuito es cuando un lado de la condicion hace que deje 
de continuar con la condicion"""

gas = False
encendido = True
edad = 19
if gas and encendido and edad > 18:
    print("Puedes avanzar")
else:
    print("mai")
