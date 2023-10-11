intentos = 1

while intentos <= 3:
    contraseña = input('Escriba la contraseña: ')
    if contraseña == 'eureka':
        print('La contraseña es correcta')
        intentos = 4
    else:
        if intentos == 3:
            print('Te has quedado sin intentos')
        else:
            print('La contraseña es incorrecta')
        intentos = intentos + 1