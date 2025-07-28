# Definimos una función llamada mostrar_multiplos_5 que no recibe parámetros
def mostrar_multiplos_5():
    # Recorremos los números del 1 al 100
    for i in range(1, 101):
        # Verificamos si el número es múltiplo de 5
        if i % 5 == 0:
            print(i)  # Si lo es, lo imprimimos

# Llamamos la función para que se ejecute
mostrar_multiplos_5()