print ("Lazo Jimeenz Angel Jesus 3W")
Num_Natural = (input("ingresar un numero natural: ")) #Le pide al usuario que ingrese un numero natural
if Num_Natural.isdigit() and int(Num_Natural) > 0:  #Esta linea verifica si el numero ingresado si es natural

    numero = int(Num_Natural) 

    if 1 <= numero <= 12: #Esta linea verifica si el numero ingresado si esta en la primera docena de numeros naturales
        print(f"El número {numero} está dentro de la primera docena de números naturales") #Si el numero si esta en la primera docena de numeros naturales le pone un mensaje al usuario de que si lo esta
    # else:
        print(f"El número {numero} no está dentro de la primera docena de números naturales") #Si no lo esta le pone al usuario que el numero no esta en la primera docena
