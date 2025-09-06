def neuronita_activadora(lista, umbral) -> bool:
    """
    Simula una neurona artificial simple.
    Activa (True) si la suma de los valores supera el umbral.
    """
    suma_total = sum(lista)
    print(f"Datos originales: {lista}")
    print(f"Umbral definido: {umbral}")
    print(f"Suma total de inputs: {suma_total}")

    if suma_total > umbral:
        print("Activación: True")
        return True
    else:
        print("Activación: False")
        return False

# Probamos con datos de ejemplo
neuronita_activadora([5, 10, 15, 20], 30)