def calculo_IMC(kg:float,altura_cm:int)->float:
    """
    Calcula el Índice de Masa Corporal (IMC).

    Args:
        kg (float): El peso de la persona en kilogramos.
        altura_cm (float): La altura de la persona en centímetros.

    Returns:
        float: El valor del IMC.
    """
    altura_metros = altura_cm / 100  # Convertir centímetros a metros
    return kg / (altura_metros ** 2)
while True:
    
 
  kg=float(input("indiqueme su peso por favor en kg :"))
  altura_cm=float(input("indiqueme su altura : "))

  imc= calculo_IMC(kg,altura_cm)
  print(f"su imc es de {imc:.2f}") 
  if imc < 18.5 :
      print("tu peso es bajo porfis come mas y toma awa")
  elif imc < 25 :
      print("estas normal wiiii")
  elif imc  < 30 :
      print("estas pachoncito cuidate porfa")
  else:
      print("estas muy pesadoo cuidadoo Dx!!!!")     
  
  continuar= input("desea verificar otro IMC s/n :").strip().lower()
  if continuar != 's':
      print("gracias vuelva pronto ")
      break