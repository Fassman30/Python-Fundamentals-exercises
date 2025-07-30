def lista_frutas(lista):
    """
    Imprime el primer y último elemento de una lista.
    """
    if lista:
        print(f"Primera fruta: {lista[0]}")
        print(f"Última fruta: {lista[-1]}")
    else:
        print("La lista está vacía.")

# Lista de ejemplo
frutas = ["manzana", "banana", "uva", "pera", "mango"]

# Llamamos la función
lista_frutas(frutas)