
def error(): #Función para mostrar mensaje de error
    print("")
    print("Opción incorrecta")
    input("\nPresione enter para continuar")
    print("\n")







def codificar(Msg,msgc,lista):

        salto = str(input("Ingrese el salto de caracteres con el que desea codificar el mensaje: "))
        if salto[0:].isdigit() == True: #Evaluar si el dato ingresado es un numero
            salto = int(salto) #Covertir el dato ingresado a entero
            
            for msg in Msg: #Pasar cada letra del mensaje principal
                    if msg in lista:  # Buscar si la letra del mensaje principal está en la lista definida inicialmente
                        # Buscar posicion del elemento en la lista definida
                        Rempla = lista.find(msg)
                        Rempla += salto  # Asignar el nuevo numero de posicion
                        while True:
                            # Analizar si el nuevo numero de posición supera la cantidad de elemtos que tiene la lista inicial
                            if Rempla >= len(lista):
                                # A la nueva posición restarle la cantidad de elementos de la lista original
                                Rempla -= len(lista)
                                continue
                            else:
                                break

                        # Asignar a la lista msgc la nueva letra
                        msgc += lista[Rempla]
                    else:
                        # En caso de que el caracter no este definido en la lista original no se le hace cambios.
                        msgc += msg            #En caso de que el caracter no este definido en la lista original no se le hace cambios.
                        
           #En caso de que el caracter no este definido en la lista original no se le hace cambios.
        else: 
            error()
            codificar(Msg,msgc,lista)
            
        msgc = msgc.replace(" ",'kl')
        msgc = msgc.replace("\n",'jl')
        encrip = open('encriptado.txt','a')
        encrip.truncate(0)
        encrip.write(msgc)
        encrip.close()
        return print("Se ha generado el archivo correctamente..."), mensaje()




def descodificar(Msg,msgc,lista): #Funcion para descodificar mensaje
            Msg = Msg.replace("kl"," ")
            Msg = Msg.replace("jl",'\n')    

            salto = str(input("Ingrese el salto de caracteres con el que se codificó el mensaje: "))
            if salto[0:].isdigit() == True: #Evaluar si el dato ingresado es un numero
                salto = int(salto)
                for msg in Msg: #Pasar cada letra del mensaje principal
                        if msg in lista:  # Buscar si la letra del mensaje principal está en la lista definida inicialmente
                            # Buscar posicion del elemento en la lista definida
                            Rempla = lista.find(msg)
                            Rempla -= salto  # Asignar el nuevo numero de posicion
                            # Analizar si el nuevo numero de posición supera la cantidad de elemtos que tiene la lista inicial
                            if Rempla >= len(lista):
                                # A la nueva posición restarle la cantidad de elementos de la lista original
                                Rempla -= len(lista)

                            while True:
                                if Rempla < 0:  # Analizar si el nuevo numero de posición supera la cantidad de elemtos que tiene la lista inicial
                                    Rempla += len(lista)
                                    continue
                                else:
                                    break

                            # Asignar a la lista msgc la nueva letra
                            msgc += lista[Rempla]
                        else:
                            # En caso de que el caracter no este definido en la lista original no se le hace cambios.
                            msgc += msg
            else:
                error()
                descodificar(Msg,msgc,lista)   
            
            
            desencrip = open('desencriptado.txt','a')
            desencrip.truncate(0)
            desencrip.write(msgc)
            desencrip.close()
            return print("Se ha generado el archivo correctamente..."), mensaje()
    
    






def mensaje(): # Funcion que muestra el mensaje de bienvenida


    print("* * * * * * * * * * * * * * * *")
    print("* Bienvenido al cifrado cesar *\n")
    print("* 1. Codificar mensaje        *")
    print("* 2. Descodificar mensaje     *")
    print("* 3. Salir                    *")
    print("* * * * * * * * * * * * * * * *")
    
    Seleccion= str(input("\nSeleccione una opción: "))
    
    if Seleccion == "1":
            f = open (str(input("Ingrese el nombre del archivo: ")+ ".txt"),'r',encoding="utf-8")
            Msg = f.read()
            f.close()


            print("\n* * * * * * * * * * * * * * * * * * * * * *")
            print("* ¿Desea utilizar una lista personalizada? \n*")
            print("* 1. Si                                     *")
            print("* 2. No                                     *")
            print("* * * * * * * * * * * * * * * * * *  * * * *")
            
            lista = str(input("\nSeleccione una opción: "))
            
            msgc =""
            
            if lista == "1":
                lista = str(input("Escriba la lista que desea utilizar, eje: 'abcde': "))
                

            elif lista == "2":
                lista ="abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNOPQRSTUVWXYZ.,:;()$%?¿!¡/+*-"


            else:
                error()
                mensaje()
                
            codificar(Msg,msgc,lista)
        
    elif Seleccion == "2":
        
        f = open (str(input("Ingrese el nombre del archivo: ")+ ".txt"),'r')
        Msg = f.read()
        Msg = Msg.replace(" ",'kl')
        Msg = Msg.replace("\n",'jl')
        f.close()
            
        print("\n* * * * * * * * * * * * * * * * * * * * * *")
        print("* ¿Desea utilizar una lista personalizada? \n*")
        print("* 1. Si                                     *")
        print("* 2. No                                     *")
        print("* * * * * * * * * * * * * * * * * *  * * * *")
            
        lista = str(input("\nSeleccione una opción: "))
            
        msgc =""
            
        if lista == "1":
                lista = str(input("Escriba la lista que desea utilizar, eje: 'abcde': "))


        elif lista == "2":
                lista ="abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNOPQRSTUVWXYZ.,:;()$%?¿!¡/+*-"


        else:
                error()
                mensaje()
                
        descodificar(Msg,msgc,lista)
        
        
    elif Seleccion == "3":
        exit() 
    else:
        error()
        mensaje()


mensaje()

