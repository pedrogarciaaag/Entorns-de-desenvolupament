x = int(input("Escriba varios numeros hasta llegar al 0 : "))

suma = 0
cont = 1

menor = x
mayor = x

while x!= 0 :
    suma = suma + x
    cont = cont + 1

    if x<menor :
        menor = x
    if x>mayor :
        mayor = x
        
    x = int(input("Escriba varios numeros hasta llegar al 0 : "))

print ("El maximo es" , mayor)
print("El minimo es" , menor)
print("La media es " , suma/(cont-1))
    