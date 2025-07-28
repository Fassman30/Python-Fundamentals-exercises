def numero_0(numero:int)->str :
       if numero <= 0 :
           print(f"gracias por usar mi programa su numero es 0 o menor{numero}")
           return # <-- Esto retorna None

while True:
    numero=int(input("escriba un numero : "))
    numero=numero_0(numero)  # <-- Aquí 'numero' se convierte en None si numero <= 0, o en None implícitamente si numero > 0
    