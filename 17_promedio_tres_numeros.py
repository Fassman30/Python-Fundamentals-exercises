def prom_tres_numeros(n1,n2,n3):
    return (n1 + n2 +n3)/3

print("****promedio de tres numeros****")
print("indique el primero numero : ")
n1 = int(input())
print("indique el segundo numero :  ")
n2 = int(input())
print("indique el tercer numero : ")
n3 = int(input())

total=prom_tres_numeros(n1,n2,n3)

print(f"el promedio es de : {total} gracias ")