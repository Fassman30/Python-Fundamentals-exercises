def descuento_edad (edad : int )-> None : #None Indica que la funcion No retorna Nada 
    """"
    Calcula el descuento segun la edad
    Parametros: 
    edad (int): edad a evaluar
    
    retorna:
    str : el resultado del descuento  segun la edad
    """

    if edad < 18 :
        print(f" años. Recibes un descuento del 25%. ")   
    elif edad <= 60:
         print(f"Tienes {edad} años. No recibes descuento, lo sentimos.")
    else :
        print(f"Tienes {edad} años. Recibes un descuento del 50% por edad mayor.")
    return edad
 
"Verificamos la edad con la entrada que el usario determine"
while True :
    try:
     edad=int(input("cual es tu edad: "))
     edad=descuento_edad(edad)
    except ValueError:
     print("ingrese un numero valido ")
    continuar=input("Desea verificar otro descuento ? (s/n): ").strip().lower()
    if continuar != 's':
        print("gracias vuelva pronto")
        break
 