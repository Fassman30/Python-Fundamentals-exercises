import math
import random 

# Definiciones de funciones
def suma() -> int:
    while True:
        try:
            numeros = input("qué números desea sumar? (sepáralos con espacio): ")
            lista_numeros = list(map(int, numeros.split()))
            return sum(lista_numeros)
        except ValueError:
            print("No es un número válido. Por favor, verifique.")
            continue

def resta() -> int:
    while True:
        try:
            numeros = input("¿Qué números desea restar? (sepáralos con espacio): ")
            lista_numeros = list(map(int, numeros.split()))
            if not lista_numeros:
                print("Por favor, ingrese al menos un número para restar.")
                continue 
            resultado = lista_numeros[0]  
            for num in lista_numeros[1:]:
                resultado -= num 
            return resultado # ¡CORRECTO! Retorna solo al final de la lógica exitosa
        except ValueError:
            print("Entrada no válida. Asegúrese de ingresar solo números separados por espacios.")
            continue
        # --- CORRECCIÓN: Captura explícitamente IndexError si la lista está vacía ---
        except IndexError:
            print("Error: No se encontraron números válidos para procesar. Intente de nuevo.")
            continue
def dividir() -> float: # Añadido el tipo de retorno
    while True:
        try:
            numeros = input("¿Qué números desea dividir? (sepárelos por espacio): ")
            lista_numeros = list(map(float,numeros.split()))
            if len(lista_numeros) < 2:
                print("Debe ingresar al menos dos números para dividir.")
                continue
            resultado = lista_numeros[0]
            for numero in lista_numeros[1:]:
                if numero == 0:
                    print("Error: No se puede dividir por cero. Por favor, ingrese un número diferente de cero.")
                    continue
                resultado /= numero
            return resultado 
        except ValueError:
            print("Dato no válido. Por favor, indique un número. Gracias.")
            continue
        except IndexError: # Para manejar si la lista está vacía o no tiene suficientes elementos
            print("Error: No se encontraron números válidos para procesar. Intente de nuevo.")
            continue
def multiplicar():
 while True:
     try:
         numeros = input("que numeros deseas multiplicar ? (separalos por espacio):")
         lista_numeros = list(map(float,numeros.split()))
         if not lista_numeros:
             print("debes ingresar almenos un numero")
             continue
         resultado=1
         for numero in lista_numeros:
             resultado *= numero
         return resultado
     except ValueError:
         print("Dato no válido. Por favor, indique un número. Gracias.")
     continue   
def salir():
    print("¡Gracias por usar la calculadora! Hasta pronto.")
       
    
# Y aquí empieza tu menú principal
while True:
    print("//////////// calculadora de funciones ////////")
    print("1: Sumar numeros")
    print("2: Restar numeros ")
    print("3: Dividir numeros")
    print("4: Multiplicar numeros")
    print("5: Salir") # ¡Agrega una opción para salir!
    opcion = input("Elija una opción por favor entre 1-5 para continuar: ")

    if opcion == '1':
        resultado = suma()
        print(f"La suma total es: {resultado}")
    elif opcion == '2':
        resultado = resta()
        print(f"La resta total es: {resultado}")
    elif opcion == '3':
        resultado = dividir()
        print(f"El resultado de la división es: {resultado}")
    elif opcion == '4':
        resultado=multiplicar()
        print(f"El resultado de la multiplicacion es: {resultado}")
    elif opcion == '5':
         salir()
         break
    else:
        print("Opción no válida. Por favor, elija un número del 1 al 5.")

    print("\n")