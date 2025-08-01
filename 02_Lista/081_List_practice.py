def frutas():
 frutas_list=["manzana","banana","cereza","datil"]
 print(f"la segunda fruta es {frutas_list[1]}")
 print(f"la ultima fruta es {frutas_list[-1]}")
 frutas_list[1]='kiwi'
 frutas_list[-1]='Naranja'
 frutas_list.pop(2)  # Elimina el elemento en la posición 2
 nueva_lista= frutas_list
 print(f"Su antigua lista era de {frutas_list}")
 print(f"su nueva lista es {nueva_lista}")
 return nueva_lista
 
frutas()