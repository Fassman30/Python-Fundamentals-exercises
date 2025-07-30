def only_greater_number(Lista,umbral):  
    new_number=[]
    for number in Lista:
        if number >  umbral:
            new_number.append(number)
    return new_number

number=[10,5,15,20,30,65,100,8,12,14,72]
resultado = only_greater_number(number,5)
print(f"the resul is {resultado}")