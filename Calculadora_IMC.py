def calcular_imc(peso, altura):
    # Calcula el IMC dividiendo el peso por el cuadrado de la altura
    return peso / (altura ** 2)

def clasificar_imc(imc):
    # Diccionario con categorías de IMC y sus rangos correspondientes
    categorias = {
        "Delgadez severa": (0, 15.9),
        "Delgadez moderada": (16.0, 16.9),
        "Delgadez leve": (17.0, 18.49),
        "Normal": (18.5, 24.9),
        "Sobrepeso": (25.0, 29.9),
        "Obesidad leve": (30.0, 34.9),
        "Obesidad media": (35, 39.0),
        "Obesidad mórbida": (40, float('inf'))
    }
    # Busca y devuelve la categoría correspondiente al IMC calculado
    for categoria, (inicio, fin) in categorias.items():
        if inicio <= imc < fin:
            return categoria

def determinar_edad(edad):
    # Devuelve el estado de edad basado en si es menor o mayor de 18 años
    return "Usted es menor de edad" if edad < 18 else "Usted es mayor de edad"

def verificar_datos(nombre, peso, altura, edad):
    # Muestra los datos ingresados y pregunta si son correctos
    print(f"\nDatos de {nombre}:\nPeso: {peso} kg\nAltura: {altura} m\nEdad: {edad} años")
    # Devuelve True si el usuario confirma que los datos son correctos
    return input("¿Son correctos? (sí/no): ").lower() in ['sí', 'si']

def calcular_peso_ideal(altura):
    # Define los límites de IMC normal
    imc_min, imc_max = 18.5, 24.9
    # Calcula el rango de peso ideal basado en la altura
    return imc_min * (altura ** 2), imc_max * (altura ** 2)

def obtener_dato_numerico(mensaje):
    # Bucle que continúa hasta que el usuario ingrese un número válido
    while True:
        try:
            # Intenta convertir la entrada del usuario a un número de punto flotante
            return float(input(mensaje))
        except ValueError:
            # Muestra un mensaje de error si la conversión falla
            print("Por favor, ingresa un número válido.")

def main():
    print("Calculadora de IMC")
    # Pregunta cuántas personas se someterán al test y se asegura de que la entrada sea numérica
    num_personas = int(obtener_dato_numerico("¿Cuántas personas se someterán al test? "))
    
    # Itera sobre el número de personas
    for i in range(num_personas):
        while True:
            print(f"\nPersona {i+1}:")
            # Solicita los datos personales y se asegura de que sean numéricos
            nombre = input("Su nombre es: ")
            peso = obtener_dato_numerico("¿Cuál es su peso en kilogramos?: ")
            altura = obtener_dato_numerico("¿Cuál es su estatura en metros?: ")
            edad = int(obtener_dato_numerico("Cuantos años tienes: "))
            
            # Verifica si los datos son correctos
            if verificar_datos(nombre, peso, altura, edad):
                break  # Sale del bucle si los datos son correctos
            else:
                print("Por favor, introduce los datos nuevamente.")
        
        # Calcula el IMC
        imc = calcular_imc(peso, altura)
        # Muestra los resultados del IMC, categoría y estado de edad
        print(f"\nResultados para {nombre}:\nIMC: {imc:.2f}\nCategoría: {clasificar_imc(imc)}\nEstado de edad: {determinar_edad(edad)}")
        
        # Pregunta si el usuario desea saber su peso ideal
        if input("¿Quieres saber cuál sería tu peso ideal aproximado? (sí/no): ").lower() in ['sí', 'si']:
            peso_ideal_min, peso_ideal_max = calcular_peso_ideal(altura)
            # Muestra el rango de peso ideal
            print(f"Peso ideal: entre {peso_ideal_min:.2f} kg y {peso_ideal_max:.2f} kg\n")
        else:
            # Agradece al usuario si no desea saber el peso ideal
            print("Gracias por haber utilizado esta calculadora de I.M.C. :) ")
    
    # Mensaje de despedida al finalizar el programa
    print(" Gracias por haber utilizado esta calculadora de I.M.C. Espero te haya sido de gran ayuda :)")

# Llama a la función principal si este script se está ejecutando
if __name__ == "__main__":
    main()