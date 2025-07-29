def sumar_y_contar( lista):
    suma_total= sum(lista)
    total_numeros=len(lista)
    print(f"la suma total es de {suma_total}")
    print(f"la cantidad de numeros es {total_numeros} ")
    return suma_total ,total_numeros
   
datos=sumar_y_contar([5, 10, 15, 20])

    