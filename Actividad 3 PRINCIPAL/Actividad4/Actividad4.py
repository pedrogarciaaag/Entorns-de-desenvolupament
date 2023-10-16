x = int(input("Escriba un numero hasta llegar al -1 : "))
suma = 0
cont = 1

while x != -1 :
    suma = suma + x
    cont = cont + 1
    x = int(input("Escriba un numero hasta llegar al -1 : "))

print("La media aritmética es " , suma/(cont-1))