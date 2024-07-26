# Input sirve para capturar datos ingresados por el usuario desde la terminal de Python sin la necesidad de nosotros haberlos definido previamente en el programa.

#La función FLOAT ( f ) devuelve una representación de coma flotante de un número. FLOAT es sinónimo de DOUBLE. El esquema es SYSIBM.

nombre = input("¿Cómo te llamas? ")
print("Hola " + nombre) # Aqui no puede ir "NOMBRE" entre comillas porque se trata de una variable y no de una cadena

edad = input("¿Cuantos años tienes?")
print(type(edad))
print(f"{nombre} tiene {edad} años")

# Programa que pide dos numeros al usuario y los suma

pregunta1 =input("¿Te gustaría jugar un juego?")
print("Increible, el juego se basa en que yo sumaré caulquier número que me pidas")
pregunta2 =input("¿Quieres empezar?")
numero1 = int(input("Introduce un número, por favor: "))
numero2 = int(input("Introduce otro número, por favor: "))
numero3 = numero1 + numero2

print(f"Tu resultado es {numero3}")
input("presione cualquier tecla para salir")