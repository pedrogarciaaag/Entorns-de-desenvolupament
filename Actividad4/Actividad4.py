A = int(input("¿Cuanto vale A? : "))
B = int(input ("¿Cuanto vale B? : "))
C = int(input ("¿Cuanto vale C? : "))
if A>B and A>C :
    print(A, "es mayor")
elif  A<B and A>=C :
    print(B , "es mayor")
elif C>A and C>=B :
    print(C , "es mayor")
elif A==C and A ==B :
    print("Son iguales")
    