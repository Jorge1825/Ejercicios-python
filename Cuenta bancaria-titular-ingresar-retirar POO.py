""" Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular y cantidad.
 El titular será obligatorio y la cantidad es opcional.
 Crea un constructor que cumpla lo anterior.
 Crear atributos
Tendrá dos métodos especiales:
 Ingresar: se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
 Retirar: se retira una cantidad a la cuenta, si restando la cantidad
 """


from os import system




while True:

    class Cuenta:
        _valor = 0
        
        def __init__(self,titular,cantidad = 0):
            
            self._titular = titular
            self._cantidad = cantidad    
            
                
                
        def Ingresar(self) :
            
            if self._cantidad < 0:
                print("La cantidad introducida es negativa, asegurese de que la cantidad no sea negativa")
            
            else:
                self._valor += self._cantidad
                print("La cantidad actual es: ", self._cantidad , "pesos")
            
            
            
            
        def Retirar(self) :
            self._valor-= self._cantidad
            
            if self._cantidad < 0:
                print("La cantidad actual es: 0 pesos")
                
            else:
                print("La cantidad actual es: ", self._cantidad , "pesos")
                
                
    











    def main():
        print("Elija una opcion:\n")
        print("1: Ingresar monto")
        print("2. Retirar monto")
        print("3. Salir")
    
        opcion = input("Ingrese una opcion: ")
        if opcion.isdigit():
            opcion = int(opcion)
            return opcion
        else:
            print("Ingrese una opcion valida")
            return main()
            
  
    
    opcion = main()
    
 
            
    if opcion == 1:
    
                print("Ingrese el titular: ")
                titular = input()
                
                if titular == "":
                    print("El titular no puede estar vacio, ingrese un titular")
                    
                    input("Presione enter para continuar")
                    system("cls")
                    main()
                    
                else:
                
                    print("Ingrese la cantidad: ")
                    
                    try:
                        cantidad = int(input())
                    except: 
                        cantidad = 0

                    finally:
        
                        if cantidad == 0:
                            cuenta = Cuenta(titular)
                            
                        else:
                            cuenta = Cuenta(titular,cantidad)
                            
            
                        cuenta.Ingresar()
                        input("Presione enter para continuar")
                        
        
    elif opcion == 2:
    
                print("Ingrese el titular: ")
                titular = input()
                
                if titular == "":
                    print("El titular no puede estar vacio, ingrese un titular")
                    
                    input("Presione enter para continuar")
                    system("cls")
                    main()
                    
                else:
                
                    print("Ingrese la cantidad: ")
                    
                    try:
                        cantidad = int(input())
                    except: 
                        cantidad = 0

                    finally:
        
                        if cantidad == 0:
                            cuenta = Cuenta(titular)
                            
                        else:
                            cuenta = Cuenta(titular,cantidad)
                            
            
                        cuenta.Ingresar()
                        input("Presione enter para continuar")
                        
        
        
    else: 
            print("Gracias por usar el programa")
            break
                

    
    system("cls")
    main()

