# Operadores aritméticos
print(2 + 2) # SUMA
print(4 - 2) # RESTA
print(3 * 7) # MULTIPLICACIÓN
print(15 / 2) # DIVISIÓN
print(11 % 4)  # ""OPERACIÓN DE MÓDULO o MÓDULO" u operador de módulo = 11 módulo 4 lo que hacemos es dividir el 11 entre 4 pero unicamente vamos a regresar el residuo el 4 unicamente cabe 2 veces (8) y el residuo es 3
print(11 // 4)  # ""OPERACIÓN DE PISO o DIVISIÓN DE PSIO" u operador de piso 11 y 2 veces el operador de piso 4 el resultado es 2 porque nos indica la cantidad de veces cabe el 4 en el 11 
        # éste tipo de operaciones son complementarios ya que en la operación de piso nos indica cuantas veces cabe el 4 de manera entera en el 11 y cual va a ser el residuo en la operación de módulo
print(2 ** 3)  # ""OPERACIÓN DE POTENCIA o POTENCIACIÓN" u operador de potencias ej. 2 al cubo es igual a 8

# operadores en cadenas de texto (strings)
print("Hola" + "mundo") # a este tipo de operaciones se les llama concatenación (cuando es suma)
print("Hola" * 3) # y aquí repetición (cuando se multiplica)
print("Hola" + "mundo" * 3)

# Operadores de comparación
print ("Hola" == "hola")  # Igual que
print ("Hola" != "hola")  # Distinto que
print (3 > 11)  # Mayor que 
print (3 < 11)  # Menor que
print (11 >= 10)  # Mayor o igual que
print (10 <= 10)  # Menor o igual que

# Operadores de existencia
print("ola" in "Hola") # Verificar si la cadena "ola" está incluida en la cadena "Hola" con "H"
print("ola" not in "Hola")  # Verificar si la cadena "ola" no está incluida en la cadena "Hola"

# Operadores Booleanos
print(True or False) # "or" es para Verificar si se cumple una de las condiciones y como hay un "True" y un "False" el resultado es True
print(True and False)  # "and" es para Verificar que se cumplan las 2 condiciones una de ellas está cumplida la cual es "True" pero la que no está cumplida es "False" así que el resultado es False

# Operadores de Asignación
x = 1 # Operador de asignación Estándar
x += 2 # Operador de asignación de suma
x *= 3  # Operador de asignación de multiplicación
x %= 4  # Operador de asignación de módulo
print(x)

x = 6 * 5 + 8 / 2 ** 4
print(x)