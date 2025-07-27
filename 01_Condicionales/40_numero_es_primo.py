def es_primo(numero:int)-> bool :
    """"
    Verificamos si el numero es primo
    Parametros numero_usu numero que se desea verificar si es primo o no
    retorna: bool si es primo o no (true o false )
    """
    if numero < 2 :
        return False
    for i in range (2,int(numero**0.5)+1):
     if numero % i == 0 :
      return  False
    return True

numero_usu=int(input("indiqueme si desea saber si un numero es primo:"))
es_primo_resultado = es_primo(numero_usu)
print(f"su numero {numero_usu} es primo  ? : {es_primo_resultado}")
