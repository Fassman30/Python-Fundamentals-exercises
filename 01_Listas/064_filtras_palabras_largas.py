def filtrar_palabras_largas(lista,umbral):
    nueva_lista= []
    for  palabra in lista:
          if len(palabra) < umbral:
             nueva_lista.append(palabra)
    return nueva_lista

palabras = ["hola", "programación", "IA", "gato", "extraordinario"]
resultado=filtrar_palabras_largas(palabras, 5)
print(f"su anterio lista era {palabras} y su nueva lista es {resultado}")