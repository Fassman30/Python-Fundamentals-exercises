def filtrar_mayores(lista, umbral):
    nueva_lista = []
    for numero in lista:
        if numero > umbral:
            nueva_lista.append(numero)
    return nueva_lista

numeros = [3, 10, 15, 2, 8]
resultado = filtrar_mayores(numeros, 7)
print(f"Mayores a 7: {resultado}")