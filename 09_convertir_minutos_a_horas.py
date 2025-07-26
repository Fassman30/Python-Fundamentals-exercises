# Definimos una función que convierte minutos a horas y minutos restantes
def convertir_minutos_horas(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes

print("**** Conversor de minutos a horas ****")
print("Indíqueme cuántos minutos desea convertir a horas:")
minutos = int(input())

horas, minutos_restantes = convertir_minutos_horas(minutos)

print(f"Las horas son: {horas}")
print(f"Los minutos de sobra son: {minutos_restantes}")