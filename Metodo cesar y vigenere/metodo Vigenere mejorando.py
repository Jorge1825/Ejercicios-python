

def error(): #Función para mostrar mensaje de error
    print("")
    print("Opción incorrecta")
    input("\nPresione enter para continuar")
    print("\n")





def codificar(Msg,msgc,lista):
        salto = input("Ingrese el mensaje clave con el que desea codificar el mensaje: ")
        i = 0 
        for msg in Msg: #Pasar cada letra del mensaje principal

                if msg in lista: 
                    salto = salto.lower()
                    clave = lista.find(salto[i % len(salto)])  #Buscar si la letra del mensaje principal está en la lista definida inicialmente
                    Rempla = lista.find(msg) #Buscar posicion del elemento en la lista definida 
                    Rempla += clave          #Asignar el nuevo numero de posicion
                    i+=1
                    if Rempla >= len(lista): #Analizar si el nuevo numero de posición supera la cantidad de elemtos que tiene la lista inicial
                        Rempla -= len(lista) #A la nueva posición restarle la cantidad de elementos de la lista original
                    msgc += lista[Rempla]    #Asignar a la lista msgc la nueva letra 
                else:
                    msgc += msg              #En caso de que el caracter no este definido en la lista original no se le hace cambios.
                    
                    
        msgc = msgc.replace(" ",'kl')
        msgc = msgc.replace("\n",'jl')
        
        encrip = open('encriptado_vigenere.txt','a')
        encrip.truncate(0)
        encrip.write(msgc)
        encrip.close()
        return print("Se ha generado el archivo correctamente..."), mensaje()

                












def descodificar(Msg,msgc,lista):
            Msg = Msg.replace("kl"," ")
            Msg = Msg.replace("jl",'\n')    

            salto = input("Ingrese el mensaje clave con el que se codificó el mensaje: ")
            i = 0
            for msg in Msg: #Pasar cada letra del mensaje principal

                        if msg in lista:   #Buscar si la letra del mensaje principal está en la lista definida inicialmente
                            salto = salto.lower()
                            clave = lista.find(salto[i % len(salto)])
                            Rempla = lista.find(msg) #Buscar posicion del elemento en la lista definida 
                            Rempla -= clave          #Asignar el nuevo numero de posicion
                            i += 1
                            if Rempla >= len(lista): #Analizar si el nuevo numero de posición supera la cantidad de elemtos que tiene la lista inicial
                                Rempla -= len(lista) #A la nueva posición restarle la cantidad de elementos de la lista original
                            msgc += lista[Rempla]    #Asignar a la lista msgc la nueva letra 
                        else:
                            msgc += msg              #En caso de que el caracter no este definido en la lista original no se le hace cambios.

            
            desen = open('desencriptado_vigenere.txt','a')
            desen.truncate(0)
            desen.write(msgc)
            desen.close()                 
            return  print("Se ha generado el archivo correctamente..."), mensaje()    



    
    
    
    
    
    
    
    
    
    
    
    

def mensaje(): # Funcion que muestra el mensaje de bienvenida



    print("* * * * * * * * * * * * * * * * * * *")
    print("* Bienvenido al cifrado de Vigenère *\n")
    print("* 1. Codificar mensaje              *")
    print("* 2. Descodificar mensaje           *")
    print("* 3. Salir                          *")
    print("* * * * * * * * * * * * * * * * * * *")
    
    
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

    
    
    
    
    
    
    
    
