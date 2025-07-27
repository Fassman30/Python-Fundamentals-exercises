def multiplo (num1 : int , num2 : int) ->bool:
   return num2 !=0 and num1 % num2 == 0
""""
Verificamos si el primer multiplo del 2
Parametros :
diviendo (int)num1: es el numero el q se desea verificar
divisor(int) num2 : el numero con el cual se verifica si es multiplo 
retorna
bool: true si es correcto o false si es incorrecto
Adicionales: se verifica los errores con try y except
"""
while True:
        try:
            num1=int(input("indiqueme el 1 numero(dividiendo) : "))
            num2=int(input("indiqueme el 2 numero (divisor):    "))
            if num2 == 0:
                print("🚫 Error: No se puede dividir entre cero.")
            elif multiplo(num1, num2):
                print(f"✅ {num1} es múltiplo de {num2}.")
            else:
                print(f"❌ {num1} NO es múltiplo de {num2}.")
        except ValueError:
            print("⚠️ Por favor, ingrese solo números válidos.")

        continuar = input("¿Desea verificar otros números? (s/n): ").strip().lower()
        if continuar != 's':
            print("👋 Gracias por usar el verificador de múltiplos.")
            break
