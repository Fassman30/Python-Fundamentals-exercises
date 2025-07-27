
 #definimos la funcion q cambie a farenheit
def cambio_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print("****cambio a fahrenheit")
print("cual son sus grados celsius C")
celsius = int(input())
farenheit=cambio_a_fahrenheit(celsius)
print(f"los grados farenheit son de : {farenheit}")
