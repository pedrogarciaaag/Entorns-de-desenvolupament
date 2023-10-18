Dia = int(input("Introduzca dia : ")) 
Mes = int(input("Introduzca mes : ")) 
if Dia>=1 and Dia<=31 :
    print("Dia valido")

    if Mes>=1 and Mes<=12 :
        print("Mes valido")
        print ("La fecha es valida")

    else :
        print("Mes no valido")
        print("La fecha es incorrecta")

else : 
    print("Dia no valido")
    if Mes>=1 and Mes<=12 :
        print("Mes valido")

    else :
        print("Mes no valido")
    print ("La fecha es incorrecta")