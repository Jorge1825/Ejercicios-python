import modelo.notas as notas
import modelo.users as users
import modelo.recoverPass as recuperarPass
import os
import re
from datetime import datetime


expeReguNom = r'^[A-Z a-z]+$'
expeRegu = r'^$'  
expresionRegularCorreo = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
exprePassword = r'^(?=.*\d)(?=.*[\u0021-\u002b\u003c-\u0040])(?=.*[A-Z])(?=.*[a-z])\S{8,16}$'


def menu():
    os.system('cls')
    print("Acciones disponibles:")
    print("1. Registro \n2. Login \n3. Salir")
    
    selecion = input("¿Que desea hacer?: ").strip()
    
    
    #Validacion de datos con expresiones regulares
    if selecion == "1" or selecion.lower() == "registro":
    
        while True:
            nombre= input("Ingrese su nombre: ").upper().strip()
            
            if re.match(expeReguNom, nombre) == None:
                
                if re.match(expeRegu, nombre):
                    nombre = "NULL"
                    break
                
                print("No es un nombre valido")
                input("Presione enter para continuar")
                continue     
            break
                
        while True:
            apellidos = input("Ingrese sus apellidos: ").upper().strip()
            
            if re.match(expeReguNom, apellidos) == None:
                if re.match(expeRegu, apellidos):
                    apellidos = "NULL"
                    break
                
                print("No es un apellido valido")
                input("Presione enter para continuar")
                continue
            break
                
        
        
        while True:
            email = input("Ingrese su correo: ").lower().strip()
            
            if re.match(expresionRegularCorreo, email) == None:
                print("No es un correo valido")
                input("Presione enter para continuar")
                continue
            break
        
        while True:
            password = input("Ingrese su contraseña: ").strip()
            password2 = input("Confirme su contraseña: ").strip()
            
            if password != password2:
                print("Las contraseñas no coinciden")
                input("Presione enter para continuar")
                continue
            
            if re.match(exprePassword, password) == None:
                print("No es una contraseña valida, la contraseña debe tener: \n-- Entre 8 y 16 caracteres \n-- Al menos una letra mayuscula \n-- Al menos una letra minuscula \n-- Al menos un numero \n-- Al menos un caracter especial")
                input("Presione enter para continuar")
                continue  
            break
        
        
        
        #Envio de datos a la base de datos   
        
        user = users.User(nombre, apellidos, email, password)  
        resultado = user.validar()
        if resultado == True:
            input("Presione enter para continuar")
            menu()
        
        input("Presiona enter para continuar")
        menu()
            
    
                
            

    elif selecion == "2" or selecion.lower() == "login":
        
        os.system("cls")
        print("Vale!! identificate en el sistema...")
        
        #Validar datos de inicio de seccion
        contador = 0
        def log(contador):
            print("\n")
            while True:
                emaillogin = input("Introce tu email: ").strip()
                if re.match(expresionRegularCorreo, emaillogin) == None:
                    print("No es un correo valido, asegurese de que este bien escrito")
                    input("Presione enter para continuar")
                    continue
                break
        
            
            while True:
                
                password3 = input("Introce tu contraseña: ").strip()
                r = users.User.validarLogin("",emaillogin, password3)
                
                if r == False:
                    contador += 1
                    
                    if contador >= 3:
                        print("\nEspere un momento...")
                        enviarcorreo = recuperarPass.EnviarCorreo(emaillogin)
                        enviarcorreo.enviarCorreo()
                    
                    log(contador)
                
                break
            
            return r, emaillogin
    
        nombrePersonatxt,emailPersona = log(contador)
        nombrePersona= nombrePersonatxt
        
        
        
        
        
        
        
        def opciones(nombrePersona,emailPersona):
            print("\tAcciones disponibles:")
            print("\t\t1. Crear nota(Crear) \n\t\t2. Mostrar notas(Mostrar) \n\t\t3. Eliminar nota(Eliminar) \n\t\t4. Modificar nota(Modificar) \n\t\t5. Cambiar contraseña(contraseña) \n\t\t6. Salir(Salir) ")
            
            opci = input("¿Que desea hacer?: ").lower().strip()
            
            if opci == "crear" or opci == "1":
                print("ok {} vamos a crear una nota".format(nombrePersona))
                
                while True:
                    titulo = input("Introduce el titulo de la nota: ").strip()
                    if re.match(r'^[ \t]*$', titulo):
                        print("No es un titulo valido")
                        input("Presione enter para continuar")
                        continue
                    
                    
                    create= notas.Nota(emailPersona)
                    t = create.validarTitulo(titulo)
                    
                    
                    if t == True:
                        os.system("cls")
                        continue
                    
                    break
                
                contenido = input("Introduce el contenido de la nota: ").strip()
                
                newNota = notas.Nota(emailPersona,titulo, contenido)
                newNota.crearNota()
                os.system("cls")
                opciones(nombrePersona,emailPersona)


                
            
            elif opci == "mostrar" or opci == "2":
                
                """Mostrar notas con el formato: 
                **************************************
                Titulo
                Contenido
                **************************
                
                """
                os.system("cls")
                print("Vale {},vamos a mostrar tus notas".format(nombrePersona))
                
                user= notas.Nota(emailPersona)
                user.MostrarNotas()
                input("Pulsa enter para continuar")
                os.system("cls")
                opciones(nombrePersona,emailPersona)
                
                
                
                
                
            elif opci == "eliminar" or opci == "3":
                print("Okey {} vamos a eliminar una nota".format(nombrePersona))
                
                Delete = input("Introduce el titulo de la nota a eliminar: ").strip()
                
                user= notas.Nota(emailPersona)
                user.EliminarNotas(Delete)
                os.system("cls")
                opciones(nombrePersona,emailPersona)
                
                
                
                
            
            elif opci == "modificar" or opci == "4":
                print("Okey {} vamos a modificar una nota".format(nombrePersona))
                
                modify = input("Introduce el titulo de la nota a modificar: ").strip()
                
                mod = notas.Nota(emailPersona)
                
    
                if mod.existenciaNota(modify) == True:
 
                    def funmodificarNota(nombrePersona,emailPersona,modify):
                        
                        print("\n¿Que desea modificar?")
                        print("\t1. Titulo \n\t2. Contenido \n\t3. Ambos")
                        
                        eleccion = input("Introduce una opcion: ").lower().strip()
                        
                        if eleccion == "titulo" or eleccion == "1":
                            newTitulo = input("Introduce el nuevo titulo: ").strip()
                            
                            newTitle= notas.Nota(emailPersona)
                            t = newTitle.validarTitulo(newTitulo)
                            
                            if t == True:
                                os.system("cls")
                                funmodificarNota(nombrePersona,emailPersona,modify)
                                
                            newTitle.modificarNota(modify,newTitulo,"1")
                            os.system("cls")
                            opciones(nombrePersona,emailPersona)
                            
                            
                        elif eleccion == "contenido" or eleccion == "2":
                            newContenido = input("Introduce el nuevo contenido: ").strip()
                            
                            newContent= notas.Nota(emailPersona)
                            newContent.modificarNota(modify,"null","2",newContenido)
                            os.system("cls")
                            opciones(nombrePersona,emailPersona)
                            
                        
                        elif eleccion == "ambos" or eleccion == "3":
                            newTitulo = input("Introduce el nuevo titulo: ").strip()
                            
                            newTitle= notas.Nota(emailPersona)
                            t = newTitle.validarTitulo(newTitulo)
                            
                            if t == True:
                                os.system("cls")
                                funmodificarNota(nombrePersona,emailPersona,modify)
                                
                            newContenido = input("Introduce el nuevo contenido: ").strip()
                            
                            newTitle.modificarNota(modify,newTitulo,"3",newContenido)
                            os.system("cls")
                            opciones(nombrePersona,emailPersona)
                            
                            
                            
                            
                        
                        else:
                            print("No es una opcion valida")
                            input("Presiona enter para continuar")
                            os.system("cls")
                            funmodificarNota(nombrePersona,emailPersona,modify)
                            
                        
                        

                    funmodificarNota(nombrePersona,emailPersona,modify)
                
                
                
                
            elif opci == "contraseña" or opci == "5":
                os.system("cls")
                print("Vale {} vamos a cambiar tu contraseña".format(nombrePersona))
                print("Este proceso cerrara sesion")
                useractual = users.User("","","",emailPersona)
                
                passactual = input("Introduce tu contraseña: ").strip()
                
    
                if useractual.validarPass(emailPersona,passactual) == False:
                    input("Presiona enter para continuar")
                    os.system("cls")
                    opciones(nombrePersona,emailPersona)
                
                else:
                

                    while True:
                        newpass = input("Introduce tu nueva contraseña: ").strip()
                        newpass2 = input("Introduce tu nueva contraseña de nuevo: ").strip()
                        
                        if newpass != newpass2:
                            print("Las contraseñas no coinciden")
                            input("Presione enter para continuar")
                            continue
                        
                        if re.match(exprePassword, newpass) == None:
                            print("No es una contraseña valida, la contraseña debe tener: \n-- Entre 8 y 16 caracteres \n-- Al menos una letra mayuscula \n-- Al menos una letra minuscula \n-- Al menos un numero \n-- Al menos un caracter especial")
                            input("Presione enter para continuar")
                            continue  
                        
                        break
                    useractual.cambiarPassword(emailPersona,newpass)
                    input("Pulsa enter para continuar")
                    menu()

                
                
            elif opci == "salir" or opci == "6":
                print("Hasta luego {}!!".format(nombrePersona))
                pass
            
            else:
                print("Opcion no valida")
                opciones(nombrePersona,emailPersona)
            
            
        opciones(nombrePersona,emailPersona)
            
        
    
    elif selecion == "3" or selecion.lower() == "salir":
        print("Gracias por preferirnos")
        pass
        
    else:
        print("Opcion no valida")
        menu()
        
menu()