def stock():
    Producto1={"Nombre":"Tacos", 
              "Precio":"150",
              "stock":True,}
    Producto2={"Nombre":"Cigarros",
               "Precio":"80",
               "stock":False,}
    Producto3={"Nombre": "Libretas",
               "Precio":"250",
               "stock":True}   
    inventario=[Producto1,Producto2,Producto3]
    for producto_actual in inventario:
        if producto_actual["stock"] is True:
            print(f"El producto {producto_actual['Nombre']} está a la venta.")
        elif producto_actual["stock"] == False:
            print(f"El producto {producto_actual['Nombre']} no está a la venta. ¡AGOTADO!")
    return producto_actual


stock()
                 