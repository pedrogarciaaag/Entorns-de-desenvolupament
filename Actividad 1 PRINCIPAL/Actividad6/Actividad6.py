A = int(input("¿Cuanto vale A? : "))
from math import sqrt
resultado = sqrt(A)
if A<=0 :
    print("Error")
else : 
    print("La raiz es : " , resultado)
    print("El cuadrado es : " , A*A)