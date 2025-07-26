def calificacion(notas: float) -> str:
    if notas >= 90 and notas <= 100:
        return "Tus notas son excelentes. ¡Felicidades! 🎉"
    elif notas >= 80 and notas < 90:
        return "Tus notas son notables "
    elif notas >= 60 and notas <= 79:
        return "Tus notas son aprobadas "
    else:
        return "Reprobaste 😢"

notas=float(input("indiqueme su nota por favor "))
notas=calificacion(notas)
print(f"{notas }")