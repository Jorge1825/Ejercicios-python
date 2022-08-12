""" Ahora a pensar!!!!: Deben programar una batalla automática entre 1 superheroe y un villano. 
La batalla durara hasta que uno de los 2 se quede sin puntos de vida. 
El daño infligido de un contrincante a otro debe ser aleatorio entre 100 y 200 puntos. 
Si desean, pueden inventar o adicionarle más cosas (poderes, escudos, etc) """


""" 
Habilidades del heroe:
1. Regenerar
2. Proteccion contra el siguiente ataque
3. Reducir el daño del oponente
4. Daño extra
5. Contra ataque

Habilidades del villano:
1. Robo de vida
2. Proteccion contra el siguiente ataque
3. Envenenar hero
4. Daño extra
5. Ataque super fuerte

"""



import random
from os import system


"""
A continuacion se crea la super Clase Personajes donde se definen 
los metodos para las clases hijas y los atributos por defecto para
las clases hijas.

Metodos:
1. ataque(): Este metodo calcula el nivrel de daño que produce el personaje al oponente. (Daño aleatorio entre 100 y 200)
2. defensa(): Este metodo calcula la defensa que tendra el personaje. (Defensa aleatoria entre 10 y 40)
3. DañoExtra(): Este metodo calcula el daño extra que produce el personaje al oponente. (Daño aleatorio entre 100 y 200)
4. GanaOPierde(): Este metodo calcula si el personaje gana o pierde el juego. (Si el personaje tiene menos puntos de vida que el oponente, gana, si no pierde)
5. __init__(): Este metodo es el constructor de la clase.


"""
class Personajes:

    def ataque(self):
        return random.randint(100, 200)

    def defensa(self):
        return random.randint(10, 40)

    def DañoExtra(self):
        return random.randint(100, 200)

    def GanaOPierde(self):
        
        if villano._vidaVillano <= 0 and heroe._vidaHero <= 0:
            print("Ambos personajes se quedaron sin vida")
            return False
        
        elif heroe._vidaHero <= 0:
            print("El heroe ha perdido :(")
            input("Presione enter para continuar")
            return False
        elif villano._vidaVillano <= 0:
            print("¡¡¡ EL HEROE HA GANADO :) !!!")
            print("El villano ha perdido")
            input("Presione enter para continuar")
            return False
        else:
            return True

    def __init__(self):
        self._vida=2000

    

    
""" 
A continuacion se crea la clase hija Heroe que hereda de la clase Personajes.
Está clase además de tener los atributos y metodos de la super clase Personajes,
tambien tiene los metodos y atributos propios de la clase Heroe.

metodos:
1. describeHabiHeroe(): Este metodo describe cada una las habilidades del heroe.
2. HabiHeroe(): Este metodo le permite al usuario selecionar las habilidades del heroe
que desea activar además evalua si hay habilidades aún disponibles.
3. __init__(): Este metodo es el constructor de la clase.
4. regenerar(): Este metodo le regenerá vida al heroe entre 250 y 320 puntos.
5. ReducirDaño(): Este metodo le da la orden al programa para que active la habilidad
de reducir daño durante el ataque del villano en las siguientes dos rondas.
6. calcularDañoReducido(): Este metodo calcula el valor de daño que reducira en el ataque del villano.
7. opciHeroe(): Este metodo se activará en caso de que la maquina deba controlar
las habilidades del heroe, por lo que la maquina elegirá por si misma qué habilidad activar.
8. msg(): Este metodo muestra un mensaje al usuario dando a conocer los puntos de vida que le restan a cada personaje.


"""    
    


class Heroe(Personajes):

    _regenerar = 1
    _proteccion = 1
    _reducir = 1
    _dañoEx = 1
    _contra = 1

    def describeHabiHeroe(self):
        print("Regenerar:\nLe permite al heroe regenerar de 250 a 350 puntos de vida.")
        print("Proteccion contra el siguiente ataque del villano:\nLe permite al heroe anular el siguiente ataque del villano.")
        print("Reducir el daño infligido por el villano:\nLe permite al heroe reducir el daño que recibira durante las siguientes dos rondas.")
        print("Daño extra:\nLe permite al heroe aumentar el daño ataque .")
        print("Contra ataque:\nLe permite al heroe devolver el doble del daño ocasionado por el villano")
        input("Presione enter para continuar")

    def HabiHeroe(self):

        system("cls")

        if self._regenerar < 1 and self._proteccion < 1 and self._reducir < 1 and self._dañoEx < 1 and self._contra < 1:
            print("No hay habilidades disponibles")
            input("Presione enter para continuar")
            return 6

        d = [[1, "Regenerar", self._regenerar],
             [2, "Proteccion contra el siguiente ataque del villano", self._proteccion],
             [3, "Reducir el daño infligido por el villano", self._reducir],
             [4, "Daño extra", self._dañoEx],
             [5, "Contra ataque", self._contra],
             [6, "Salir/Ninguna", ""],
             [7, "Información de las habilidades del heroe", ""]]

        print("{:<8} {:<55} {:<10}".format(
            'Opción', 'Habilidad', 'Numero de oportunidades'))
        print("{:<8} {:<55} {:<10}".format(
            '------', '---------', '-----------------------'))
        for i in d:
            name, age, perc = i
            print("{:<8} {:<65} {:<10}".format(name, age, perc))

        ele = input("Ingrese el numero de la opcion que desea:  ")
        if ele.isdigit():
            ele = int(ele)
            if ele < 1 or ele > 7:
                print("Ingrese una opcion valida")
                input("Presione enter para continuar")
                return self.HabiHeroe()

            elif ele == 1 and self._regenerar > 0:
                self._regenerar -= 1
                return ele

            elif ele == 2 and self._proteccion > 0:
                self._proteccion -= 1
                return ele
            elif ele == 3 and self._reducir > 0:
                self._reducir -= 1
                return ele
            elif ele == 4 and self._dañoEx > 0:
                self._dañoEx -= 1
                return ele
            elif ele == 5 and self._contra > 0:
                self._contra -= 1
                return ele
            elif ele == 6:
                return ele

            elif ele == 7:
                self.describeHabiHeroe()
                return self.HabiHeroe()
            else:
                print("La habilidad no está disponible")
                input("Presione enter para continuar")
                return self.HabiHeroe()
        else:
            print("Ingrese una opcion valida")
            input("Presione enter para continuar")
            return self.HabiHeroe()

    def __init__(self,):
        super().__init__()
        self._vidaHero = self._vida
        self._rondaDaño = 0
        self._habiHeroe = [1,2,3,4,5,6]

    def regenerar(self):
        r = random.randint(250, 320)
        heroe._vidaHero += r

        print(f"El heroe ha regenerado {r} puntos de vida")

    def ReducirDaño(self):
        self._rondaDaño = 2
        print("El heroe ha activado la habilidad de reducir el daño durante las siguientes dos rondas")

    def calcularDañoReducido(self):
        r = random.randint(40, 60)
        return r
    
    
    def opciHeroe(self):

        if len(self._habiHeroe) <=1:
            return 6
            
        else:
            ran = random.choice(self._habiHeroe)
            self._habiHeroe.remove(ran)
 
            if ran == 1 and self._regenerar > 0:
                self._regenerar -= 1
                return ran

            elif ran == 2 and self._proteccion > 0:
                self._proteccion -= 1
                return ran
            elif ran == 3 and self._reducir > 0:
                self._reducir -= 1
                return ran
            elif ran == 4 and self._dañoEx > 0:
                self._dañoEx -= 1
                return ran
            elif ran == 5 and self._contra > 0:
                self._contra -= 1
                return ran
            else:
                return ran

    
    
    
    def msg(self):
        if villano._vidaVillano < 0:
            villano._vidaVillano = 0
        if heroe._vidaHero < 0:
            heroe._vidaHero = 0
        
        print("El Villano tiene: ", villano._vidaVillano, "de vida")
        print("El Heroe tiene: ", heroe._vidaHero, "de vida\n")
        input("Presione enter para continuar")
    
    
 
 
 
 
 
 
 
""" 
A continuacion se crea la clase hija Heroe que hereda de la clase Personajes.
Está clase además de tener los atributos y metodos de la super clase Personajes,
tambien tiene los metodos y atributos propios de la clase Heroe.

metodos:
1. describeHabiVilla(): Este metodo describe cada una las habilidades del Villano.
2. Habivillano(): Este metodo le permite al usuario selecionar las habilidades del villano
que desea activar además evalua si hay habilidades aún disponibles.
3. __init__(): Este metodo es el constructor de la clase.
4. roboVida(): Este metodo le regenerá vida al villano robando entre 150 y 200 puntos de vida del heroe.
5. envenenarHero: Este metodo le da la orden al programa para que active la habilidad
de envenenar al heroe durante el ataque del heroe en las siguientes dos rondas.
6. AtaqueSuperFuerte: Este metodo calcula el valor de daño adicional que infligirá al heroe.
7. calcular el daño por envenenar():Este metodo calcula el daño que infligirá al heroe si la habilidad de envenenar está activa 
8. opciVilla()Este metodo se activará en caso de que la maquina deba controlar
las habilidades del heroe, por lo que la maquina elegirá por si misma qué habilidad activar.
8. msg2(): Este metodo muestra un mensaje al usuario dando a conocer los puntos de vida que le restan a cada personaje.


"""   

 
    


class Villano(Personajes):

    _roboVida = 1
    _proteccionVilla = 1
    _envenenar = 1
    _dañoExVilla = 1
    _ataqueSuper = 1

    def describeHabiVilla(self):
        print("Robo de vida:\nLe permite al villano robar entre 200 y 250 puntos de vida.")
        print("Proteccion contra el siguiente ataque del heroe:\nLe permite al villano anular el siguiente ataque del heroe.")
        print("Envenenar:\nCuando el villano active está habilidad, el heroe se envenenará y perdera entre 20 y 50 puntos de vida durante las siguientes dos rondas.")
        print("Daño extra:\nLe permite al villano aumentar el daño ataque .")
        print("Ataque super fuerte:\nLe permite al villano infligir un daño extra al heroe entre 100 y 200 puntos de vida.")
        input("Presione enter para continuar")

    def HabiVillano(self):

        system("cls")

        if self._roboVida < 1 and self._proteccionVilla < 1 and self._envenenar < 1 and self._dañoExVilla < 1 and self._ataqueSuper < 1:
            print("No hay habilidades disponibles")
            input("Presione enter para continuar")
            return 6

        d = [[1, "Robo de vida", self._roboVida],
             [2, "Proteccion contra el siguiente ataque del heroe",
                 self._proteccionVilla],
             [3, "Envenenar heroe", self._envenenar],
             [4, "Daño extra", self._dañoExVilla],
             [5, "Ataque super fuerte", self._ataqueSuper],
             [6, "Salir", ""],
             [7, "Información de las habilidades del villano", ""]]

        print("{:<8} {:<55} {:<10}".format(
            'Opción', 'Habilidad', 'Numero de oportunidades'))
        print("{:<8} {:<55} {:<10}".format(
            '------', '---------', '-----------------------'))
        for i in d:
            name, age, perc = i
            print("{:<8} {:<65} {:<10}".format(name, age, perc))

        ele = input("Ingrese el numero de la opcion que desea:  ")
        if ele.isdigit():
            ele = int(ele)
            if ele < 1 or ele > 7:
                print("Ingrese una opcion valida")
                input("Presione enter para continuar")
                return self.HabiVillano()

            elif ele == 1 and self._roboVida > 0:
                self._roboVida -= 1
                return ele
            
            elif ele == 2 and self._proteccionVilla > 0:
                self._proteccionVilla -= 1
                return ele
            
            elif ele == 3 and self._envenenar > 0:
                self._envenenar -= 1
                return ele
            
            elif ele == 4 and self._dañoExVilla > 0:
                self._dañoExVilla -= 1
                return ele
            
            elif ele == 5 and self._ataqueSuper > 0:
                self._ataqueSuper -= 1
                return ele
            
            elif ele == 6:
                return ele

            elif ele == 7:
                self.describeHabiVilla()
                return self.HabiVillano()

            else:
                print("La habilidade no está disponible")
                input("Presione enter para continuar")
                return self.HabiVillano()
        else:
            print("Ingrese una opcion valida")
            input("Presione enter para continuar")
            return self.HabiVillano()

    def __init__(self):
        super().__init__()
        self._vidaVillano = self._vida
        self._rondaEnvenenar = 0
        self._habiVilla = [1, 2, 3, 4, 5, 6]

    def roboVida(self):
        r = random.randint(170, 220)
        heroe._vidaHero -= r
        villano._vidaVillano += r

        print(f"El villano ha robado {r} puntos de vida")

    def envenenarHero(self):
        self._rondaEnvenenar = 2
        print("El villano ha activado la habilidad de envenenar al heroe y lo envenenará durante las siguientes dos rondas")

    def ataqueSuperFuerte(self):
        r = random.randint(100, 200)
        print(f"El villano ha realizado un ataque super fuerte y ha infligido {r} puntos de vida adicional")
        return r

    def calcularDañoPorEnvenenar(self):
        r = random.randint(20, 40)
        return r

    def opciVilla(self):

        if len(self._habiVilla) <=1:
            return 6
        else:

            ran = random.choice(self._habiVilla)
            self._habiVilla.remove(ran)

            if ran == 1 and self._roboVida > 0:
                self._roboVida -= 1
                return ran
                
            elif ran == 2 and self._proteccionVilla > 0:
                self._proteccionVilla -= 1
                return ran
                
            elif ran == 3 and self._envenenar > 0:
                self._envenenar -= 1
                return ran
                
            elif ran == 4 and self._dañoExVilla > 0:
                self._dañoExVilla -= 1
                return ran
                
            elif ran == 5 and self._ataqueSuper > 0:
                self._ataqueSuper -= 1
                return ran
                
            else:
                return ran

    
    def msg2(self):
        if villano._vidaVillano < 0:
            villano._vidaVillano = 0
        if heroe._vidaHero < 0:
            heroe._vidaHero = 0
        print("El Heroe tiene: ", heroe._vidaHero, "de vida")
        print("El Villano tiene: ", villano._vidaVillano, "de vida\n")
        input("Presione enter para continuar")









"""
Desde este punto se analizan los datos que el usuario ingresa y hace su respectiva funcion
"""








while True:

    """
    Funcion que se encarga de mostrar el menu de opciones al usuario 
    y retorna el numero de la opcion que selecciona
    """
    def main():

        system("cls")
        print("Bienvenido a la batalla")
        print("¿Qué personaje quieres ser?")
        print("1. Heroe")
        print("2. Villano")

        personaje = input("Ingrese una opcion: ")
        if personaje.isdigit():
            personaje = int(personaje)
            if personaje < 1 or personaje > 2:
                print("Ingrese una opcion valida")
                input("Presione enter para continuar")
                return main()
            else:
                return personaje
        else:
            print("Ingrese una opcion valida")
            input("Presione enter para continuar")
            return main()

    pers = main()
    
    
    
    
    
    """
    Sentencias para evaluar la opcion que el usuario ingresa
    """
    

    if pers == 1:
        print("Has elegido un Heroe")
        #Creacion de objetos 
        heroe = Heroe()
        villano = Villano()

        #Inicio de la batalla, mientras el heroe y el villano tienen vida se ejecutara el ciclo
        while heroe._vidaHero > 0 and villano._vidaVillano > 0:
            
            #Obtencion del valor de habilidad 
            habi = heroe.HabiHeroe()
            habi2 = villano.opciVilla()
            
            
            #If en caso de que el heroe no tenga ninguna habilidad disponible
            if heroe._regenerar == 0 and heroe._proteccion == 0 and heroe._reducir == 0 and heroe._dañoEx == 0 and heroe._contra == 0:

                if heroe._rondaDaño > 0:            
                    heroe._rondaDaño -= 1
                    
                    if habi2 == 1:
                        villano.roboVida()
                        print("El Heroe ha robado vida")
                        if villano._rondaEnvenenar > 0:
                            
                            villano._rondaEnvenenar -= 1  
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                            


                        else:

                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= (villano.ataque() - heroe.calcularDañoReducido())

                        


        
                    
                    elif habi2 == 2:
                        print("El villano ha activado la habilidad de proteccion")
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                            


                        else:
                            heroe._vidaHero -= (villano.ataque() - heroe.calcularDañoReducido())
                        


                    
                    
                    elif habi2 == 3:
                        print("El villano ha activado la habilidad de envenenar")
                        villano.envenenarHero()
                        villano._rondaEnvenenar -= 1
                        villano._vidaVillano -= heroe.ataque()
                        heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                        



                    
                    
                    
                    elif habi2 == 4:
                        print("El villano ha activado la habilidad de aumentar el daño")
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.DañoExtra() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                            


                        else:
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.DañoExtra()) - heroe.calcularDañoReducido())
                            
                        


                    
                    
                    elif habi2 == 5:
                        print("El villano ha activado la habilidad de super ataque")
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                            


                        else:
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.ataqueSuperFuerte()) - heroe.calcularDañoReducido())
                            
                            
                            
                    
                    else:
                        
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                            

                        else:

                            heroe._vidaHero -= villano.ataque() - heroe.calcularDañoReducido()
                            villano._vidaVillano -= heroe.ataque()
                            
                        
                    ganaono = heroe.GanaOPierde()
                    
                    if ganaono == False:
                        break
                    
                    heroe.msg()    
                        
                        

                    
                #Else del if sin habilidades
                else:
                    if habi2 == 1:
                        villano.roboVida()
                        print("El Heroe ha robado vida")
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1  
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                    

                        else:

                            
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= villano.ataque()

                    
                    
                    elif habi2 == 2:
                        print("El villano ha activado la habilidad de proteccion")
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                            


                        else:
                            heroe._vidaHero -= villano.ataque()
                        
                        
                    
                    elif habi2 == 3:
                        print("El villano ha activado la habilidad de envenenar")
                        villano.envenenarHero()
                        villano._rondaEnvenenar -= 1
                        villano._vidaVillano -= heroe.ataque()
                        heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                        

                    
                    elif habi2 == 4:
                        print("El villano ha activado la habilidad de aumentar el daño")
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= (villano.ataque() + villano.DañoExtra() + villano.calcularDañoPorEnvenenar())
                            


                        else:
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= (villano.ataque() + villano.DañoExtra())
                            
                        
                    
                    elif habi2 == 5:
                        print("El villano ha activado la habilidad de super ataque")
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= (villano.ataque() + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())
                            


                        else:
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= (villano.ataque() + villano.ataqueSuperFuerte()) 
                            
                            
                            
                        
                    
                    else:
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                            

                        else:

                            heroe._vidaHero -= villano.ataque() 
                            villano._vidaVillano -= heroe.ataque()
                            
                        

                    ganaono = heroe.GanaOPierde()
                    if ganaono == False:
                        break

                    heroe.msg()














#Else principal, este else se ejecuta cuando el heroe tiene habilidades disponibles
            else:
#Codigo de la habilidad 1
                if habi == 1:
                    heroe.regenerar()
                    if heroe._rondaDaño > 0:
                        heroe._rondaDaño -= 1
                    
                        if habi2 == 1:
                            villano.roboVida()
                            print("El villano ha robado vida")
                            if villano._rondaEnvenenar > 0:
                                
                                villano._rondaEnvenenar -= 1  
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                


                            else:

                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() - heroe.calcularDañoReducido())


                            
            
                        
                        elif habi2 == 2:
                            print("El villano ha activado la habilidad de proteccion")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                                


                            else:
                                heroe._vidaHero -= (villano.ataque() - heroe.calcularDañoReducido())
                            
                            


                        
                        
                        elif habi2 == 3:
                            print("El villano ha activado la habilidad de envenenar")
                            villano.envenenarHero()
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                            




                        
                        
                        
                        elif habi2 == 4:
                            print("El villano ha activado la habilidad de aumentar el daño")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.DañoExtra() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                                


                            else:
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.DañoExtra()) - heroe.calcularDañoReducido())
                                
                            



                        
                        
                        elif habi2 == 5:
                            print("El villano ha activado la habilidad de super ataque")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                


                            else:
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.ataqueSuperFuerte()) - heroe.calcularDañoReducido())
                                
                                
                                



                        
                        
                        else:
                            
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                

                            else:

                                heroe._vidaHero -= villano.ataque() - heroe.calcularDañoReducido()
                                villano._vidaVillano -= heroe.ataque()
                                

                            
                        ganaono = heroe.GanaOPierde()
                        if ganaono == False:
                            break
                        
                        heroe.msg() 
                    



#Else de la habilidad 1
                    else:
                        if habi2 == 1:
                            villano.roboVida()
                            print("El villano ha robado vida")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1  
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                        

                            else:

                                
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= villano.ataque()

                        
                        elif habi2 == 2:
                            print("El villano ha activado la habilidad de proteccion")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                heroe._vidaHero -= villano.ataque()
                            
                            
                        
                        elif habi2 == 3:
                            print("El villano ha activado la habilidad de envenenar")
                            villano.envenenarHero()
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                            

                        
                        elif habi2 == 4:
                            print("El villano ha activado la habilidad de aumentar el daño")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.DañoExtra() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.DañoExtra())
                                
                            
                        
                        elif habi2 == 5:
                            print("El villano ha activado la habilidad de super ataque")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.ataqueSuperFuerte()) 
                                
                                
                                
                            
                        
                        else:
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                                

                            else:

                                heroe._vidaHero -= villano.ataque() 
                                villano._vidaVillano -= heroe.ataque()
                                
                            

                        ganaono = heroe.GanaOPierde()
                        if ganaono == False:
                            break

                        heroe.msg()
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        

#Codigo para la habilidad numero 2

                elif habi == 2:
                    if heroe._rondaDaño > 0:
                        heroe._rondaDaño -= 1


                    if habi2 == 1:
                            villano.roboVida()
                            print("El villano ha robado vida")
                            if villano._rondaEnvenenar > 0:
                                
                                villano._rondaEnvenenar -= 1  
                                villano._vidaVillano -= heroe.ataque()
                                
                                


                            else:

                                villano._vidaVillano -= heroe.ataque()


                            
            
                        
                    elif habi2 == 2:
                            print("El villano ha activado la habilidad de proteccion")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                            

                        
                        
                        
                        
                    elif habi2 == 3:
                            print("El villano ha activado la habilidad de envenenar")    
                            villano.envenenarHero()
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()




                        
                        
                        
                    elif habi2 == 4:
                            print("El villano ha activado la habilidad de aumentar el daño")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                              


                            else:
                                villano._vidaVillano -= heroe.ataque()
       
                            


                        
                        
                    elif habi2 == 5:
                            print("El villano ha activado la habilidad de super ataque")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
               

                            else:
                                villano._vidaVillano -= heroe.ataque()
                                                
                                


                        
                        
                    else:
                            
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
             

                            else:

                                villano._vidaVillano -= heroe.ataque()
                                
                            
                    ganaono = heroe.GanaOPierde()    
                    if ganaono == False:
                            break
                        
                    heroe.msg()



















#Codigo de la habilidad numero 3
                elif habi == 3:
                    heroe.ReducirDaño()
                    heroe._rondaDaño -= 1
                    
                    if habi2 == 1:
                        villano.roboVida()
                        print("El villano ha robado vida")
                        if villano._rondaEnvenenar > 0:
                            
                            villano._rondaEnvenenar -= 1  
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                            


                        else:

                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= (villano.ataque() - heroe.calcularDañoReducido())

                       


                        
        
                    
                    elif habi2 == 2:
                        print("El villano ha activado la habilidad de proteccion")
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                            


                        else:
                            heroe._vidaHero -= (villano.ataque() - heroe.calcularDañoReducido())
                        
                        

                    
                    
                    elif habi2 == 3:
                        print("El villano ha activado la habilidad de envenenar")
                        villano.envenenarHero()
                        villano._rondaEnvenenar -= 1
                        villano._vidaVillano -= heroe.ataque()
                        heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                        



                    
                    
                    
                    elif habi2 == 4:
                        print("El villano ha activado la habilidad de aumentar el daño")
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.DañoExtra() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                            


                        else:
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.DañoExtra()) - heroe.calcularDañoReducido())
                            
                        


                    
                    
                    elif habi2 == 5:
                        print("El villano ha activado la habilidad de super ataque")
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                            


                        else:
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.ataqueSuperFuerte()) - heroe.calcularDañoReducido())
                            
                            
                            


                    
                    
                    else:
                        
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                            

                        else:

                            heroe._vidaHero -= villano.ataque() - heroe.calcularDañoReducido()
                            villano._vidaVillano -= heroe.ataque()
                            
                        
                    ganaono = heroe.GanaOPierde()
                    if ganaono == False:
                        break
                    
                    heroe.msg()
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
#Codigo de la habilidad numero 4
                elif habi == 4:

                    if heroe._rondaDaño > 0:
                        heroe._rondaDaño -= 1
                        
                        if habi2 == 1:
                            villano.roboVida()
                            print("El villano ha robado vida")
                            if villano._rondaEnvenenar > 0:
                                
                                villano._rondaEnvenenar -= 1  
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                


                            else:

                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= (villano.ataque() - heroe.calcularDañoReducido())


                            
            
                        
                        elif habi2 == 2:
                            print("El villano ha activado la habilidad de proteccion")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                                


                            else:
                                heroe._vidaHero -= (villano.ataque() - heroe.calcularDañoReducido())
                            
                            

                        
                        
                        elif habi2 == 3:
                            
                            villano.envenenarHero()
                            print("El villano ha activado la habilidad de envenenar")
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                            heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                            



                        
                        
                        
                        elif habi2 == 4:
                            print("El villano ha activado la habilidad de aumentar el daño")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= ((villano.ataque() + villano.DañoExtra() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                                


                            else:
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= ((villano.ataque() + villano.DañoExtra()) - heroe.calcularDañoReducido())
                                
                            


                        
                        
                        elif habi2 == 5:
                            print("El villano ha activado la habilidad de super ataque")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= ((villano.ataque() + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                


                            else:
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= ((villano.ataque() + villano.ataqueSuperFuerte()) - heroe.calcularDañoReducido())
                                
                                
                                


                        
                        
                        else:
                            
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                

                            else:

                                heroe._vidaHero -= villano.ataque() - heroe.calcularDañoReducido()
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                
                            
                        ganaono = heroe.GanaOPierde()
                        if ganaono == False:
                            break
                        
                        heroe.msg() 
                
                
                
                
#Else de la opcion de habilidad 4 
                    else:

                        if habi2 == 1:
                            villano.roboVida()
                            print("El villano ha robado vida")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1  
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                        

                            else:

                                
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= villano.ataque()

                            
                        
                        elif habi2 == 2:
                            print("El villano ha activado la habilidad de proteccion")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                heroe._vidaHero -= villano.ataque()
                            
                            
                        
                        elif habi2 == 3:
                            print("El villano ha activado la habilidad de envenenar")
                            villano.envenenarHero()
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                            heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                            

                        
                        elif habi2 == 4:
                            print("El villano ha activado la habilidad de aumentar el daño")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= (villano.ataque() + villano.DañoExtra() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= (villano.ataque() + villano.DañoExtra())
                                
                            
                        
                        elif habi2 == 5:
                            print("El villano ha activado la habilidad de super ataque")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= (villano.ataque() + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= (villano.ataque() + villano.ataqueSuperFuerte()) 
                                
                                
                                
                            
                        
                        else:
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                                

                            else:

                                heroe._vidaHero -= villano.ataque() 
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                
                            

                        ganaono = heroe.GanaOPierde()
                        if ganaono == False:
                            break

                        heroe.msg()



















#Codigo de habilida numero 5
                elif habi == 5:
                    if heroe._rondaDaño > 0:
                        heroe._rondaDaño -= 1

                        contra = heroe.ataque() 

                        if habi2 == 1:
                            villano.roboVida()
                            print("El villano ha robado vida")
                            if villano._rondaEnvenenar > 0:
                                
                                villano._rondaEnvenenar -= 1  
                                villano._vidaVillano -= contra * 2.5
                                heroe._vidaHero -= ((contra + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                


                            else:

                                villano._vidaVillano -= contra * 2.5
                                heroe._vidaHero -= (contra - heroe.calcularDañoReducido())

                            
            
                        
                        elif habi2 == 2:
                            print("El villano ha activado la habilidad de proteccion")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                heroe._vidaHero -= ((contra + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                                


                            else:
                                heroe._vidaHero -= (contra - heroe.calcularDañoReducido())
                            


                        
                        
                        elif habi2 == 3:
                            print("El villano ha activado la habilidad de envenenar")
                            villano.envenenarHero()
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= contra * 2.5
                            heroe._vidaHero -= ((contra + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                            

                        
                        
                        elif habi2 == 4:
                            print("El villano ha activado la habilidad de aumentar el daño")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= contra * 2.5
                                heroe._vidaHero -= ((contra + villano.DañoExtra() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                                


                            else:
                                villano._vidaVillano -= contra * 2.5
                                heroe._vidaHero -= ((contra + villano.DañoExtra()) - heroe.calcularDañoReducido())
                                
                            
                        
                        
                        elif habi2 == 5:
                            print("El villano ha activado la habilidad de super ataque")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= contra * 2.5
                                heroe._vidaHero -= ((contra + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                


                            else:
                                villano._vidaVillano -= contra * 2.5
                                heroe._vidaHero -= ((contra + villano.ataqueSuperFuerte()) - heroe.calcularDañoReducido())
                                



                        
                        
                        else:
                            
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= contra * 2.5
                                heroe._vidaHero -= ((contra + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                

                            else:

                                heroe._vidaHero -= contra - heroe.calcularDañoReducido()
                                villano._vidaVillano -= contra * 2.5
                                
                        
                        ganaono = villano.GanaOPierde()    
                        
                        if ganaono == False:
                            break
                        
                        heroe.msg()

                    





#Else de habilidad 5
                    else: 
                        contra = heroe.ataque()
                        

                        if habi2 == 1:
                            villano.roboVida()
                            print("El villano ha robado vida")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1  
                                villano._vidaVillano -= contra * 2
                                heroe._vidaHero -= (contra + villano.calcularDañoPorEnvenenar())
                        

                            else:

                                
                                villano._vidaVillano -= contra * 2
                                heroe._vidaHero -= contra


                        
                        elif habi2 == 2:
                            print("El villano ha activado la habilidad de proteccion")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                heroe._vidaHero -= (contra + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                heroe._vidaHero -= contra
                            
                            

                        
                        elif habi2 == 3:
                            print("El villano ha activado la habilidad de envenenar")
                            villano.envenenarHero()
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= contra * 2
                            heroe._vidaHero -= (contra + villano.calcularDañoPorEnvenenar())
                            


                        
                        elif habi2 == 4:
                            print("El villano ha activado la habilidad de aumentar el daño")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= contra * 2
                                heroe._vidaHero -= (contra + villano.DañoExtra() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                villano._vidaVillano -= contra * 2
                                heroe._vidaHero -= (contra + villano.DañoExtra())
                                

                        
                        elif habi2 == 5:
                            print("El villano ha activado la habilidad de super ataque")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= contra * 2
                                heroe._vidaHero -= (contra + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                villano._vidaVillano -= contra * 2
                                heroe._vidaHero -= (contra + villano.ataqueSuperFuerte()) 
                                
                                
  
                            
                        
                        else:
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= contra * 2
                                heroe._vidaHero -= (contra + villano.calcularDañoPorEnvenenar())
                                

                            else:

                                heroe._vidaHero -= contra 
                                villano._vidaVillano -= contra * 2
                                
                        
                        
                        ganaono = villano.GanaOPierde()
                        
                        if ganaono == False:
                            break

                        heroe.msg()










#Codigo de la habilidad 6
                else:
                    
                    if heroe._rondaDaño > 0:
                        heroe._rondaDaño -= 1


                    
                        if habi2 == 1:
                            villano.roboVida()
                            print("El villano ha robado vida")
                            if villano._rondaEnvenenar > 0:
                                
                                villano._rondaEnvenenar -= 1  
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                


                            else:

                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() - heroe.calcularDañoReducido())

                            


            
                        
                        elif habi2 == 2:
                            print("El villano ha activado la habilidad de proteccion")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                                


                            else:
                                heroe._vidaHero -= (villano.ataque() - heroe.calcularDañoReducido())
                            


                        
                        
                        elif habi2 == 3:
                            print("El villano ha activado la habilidad de envenenar")
                            villano.envenenarHero()
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                            



                        
                        
                        
                        elif habi2 == 4:
                            print("El villano ha activado la habilidad de aumentar el daño")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.DañoExtra() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                                


                            else:
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.DañoExtra()) - heroe.calcularDañoReducido())
                                
                            


                        
                        
                        elif habi2 == 5:
                            print("El villano ha activado la habilidad de super ataque")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                


                            else:
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.ataqueSuperFuerte()) - heroe.calcularDañoReducido())
                                
                                
                                


                        
                        
                        else:
                            
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                

                            else:

                                heroe._vidaHero -= villano.ataque() - heroe.calcularDañoReducido()
                                villano._vidaVillano -= heroe.ataque()
                                
                            
                        ganaono = heroe.GanaOPierde()
                        
                        if ganaono == False:
                            break
                        
                        heroe.msg()





#Else de la habilidad 6
                    else:


                        if habi2 == 1:
                            villano.roboVida()
                            print("El villano ha robado vida")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1  
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                        

                            else:

                                
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= villano.ataque()

                        
                        
                        elif habi2 == 2:
                            print("El villano ha activado la habilidad de proteccion")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                heroe._vidaHero -= villano.ataque()
                            
                            
                        
                        elif habi2 == 3:
                            print("El villano ha activado la habilidad de envenenar")
                            villano.envenenarHero()
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                            

                        
                        elif habi2 == 4:
                            print("El villano ha activado la habilidad de aumentar el daño")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.DañoExtra() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.DañoExtra())
                                
                            
                        
                        elif habi2 == 5:
                            print("El villano ha activado la habilidad de super ataque")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.ataqueSuperFuerte()) 
                                
                                
                                
                            
                        
                        else:
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                                

                            else:

                                heroe._vidaHero -= villano.ataque() 
                                villano._vidaVillano -= heroe.ataque()
                                
                            

                        ganaono = heroe.GanaOPierde()
                        if ganaono == False:
                            break

                        heroe.msg()

        
        
        
        break













        """ 
        Desde este punto se empiezan a codificar todas las habilidades
        para el villano, pero dicho codigo se ha copiado y pegado de las
        habilidades del heroe ya que son las mismas solo se ha cambiado el
        orden con el que la vida deciende, ya que en este caso el villano
        tiene la oportunidad de realizar el primer golpe.
        """








# Codigo para el villano, este else se ejecuta cuando el usuario elige el villano
    else:
        print("Has elegido Villano")
        heroe = Heroe()
        villano = Villano()

        while heroe._vidaHero > 0 and villano._vidaVillano > 0:
            habi = heroe.opciHeroe()
            habi2 = villano.HabiVillano()
            if heroe._regenerar == 0 and heroe._proteccion == 0 and heroe._reducir == 0 and heroe._dañoEx == 0 and heroe._contra == 0:

                if heroe._rondaDaño > 0:            
                    heroe._rondaDaño -= 1
                    
                    if habi2 == 1:
                        villano.roboVida()
                        print("El Heroe ha robado vida")
                        if villano._rondaEnvenenar > 0:
                            
                            villano._rondaEnvenenar -= 1  
                            heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                            villano._vidaVillano -= heroe.ataque()
                            
                            


                        else:
                            heroe._vidaHero -= (villano.ataque() - heroe.calcularDañoReducido())
                            villano._vidaVillano -= heroe.ataque()
                            

                        


        
                    
                    elif habi2 == 2:
                        print("El villano ha activado la habilidad de proteccion")
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                            


                        else:
                            heroe._vidaHero -= (villano.ataque() - heroe.calcularDañoReducido())
                        


                    
                    
                    elif habi2 == 3:
                        print("El villano ha activado la habilidad de envenenar")
                        villano.envenenarHero()
                        villano._rondaEnvenenar -= 1
                        heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                        villano._vidaVillano -= heroe.ataque()
                        
                        



                    
                    
                    
                    elif habi2 == 4:
                        print("El villano ha activado la habilidad de aumentar el daño")
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.DañoExtra() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                            


                        else:
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.DañoExtra()) - heroe.calcularDañoReducido())
                            
                        


                    
                    
                    elif habi2 == 5:
                        print("El villano ha activado la habilidad de super ataque")
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                            


                        else:
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.ataqueSuperFuerte()) - heroe.calcularDañoReducido())
                            
                            
                            
                    
                    else:
                        
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                            

                        else:

                            heroe._vidaHero -= villano.ataque() - heroe.calcularDañoReducido()
                            villano._vidaVillano -= heroe.ataque()
                            
                        
                    ganaono = heroe.GanaOPierde()
                    
                    if ganaono == False:
                        break
                    
                    villano.msg2()    
                        
                        

                    
                #Else del if sin habilidades
                else:
                    if habi2 == 1:
                        villano.roboVida()
                        print("El Heroe ha robado vida")
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1  
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                    

                        else:

                            
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= villano.ataque()

                    
                    
                    elif habi2 == 2:
                        print("El villano ha activado la habilidad de proteccion")
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                            


                        else:
                            heroe._vidaHero -= villano.ataque()
                        
                        
                    
                    elif habi2 == 3:
                        print("El villano ha activado la habilidad de envenenar")
                        villano.envenenarHero()
                        villano._rondaEnvenenar -= 1
                        villano._vidaVillano -= heroe.ataque()
                        heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                        

                    
                    elif habi2 == 4:
                        print("El villano ha activado la habilidad de aumentar el daño")
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= (villano.ataque() + villano.DañoExtra() + villano.calcularDañoPorEnvenenar())
                            


                        else:
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= (villano.ataque() + villano.DañoExtra())
                            
                        
                    
                    elif habi2 == 5:
                        print("El villano ha activado la habilidad de super ataque")
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= (villano.ataque() + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())
                            


                        else:
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= (villano.ataque() + villano.ataqueSuperFuerte()) 
                            
                            
                            
                        
                    
                    else:
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                            

                        else:

                            heroe._vidaHero -= villano.ataque() 
                            villano._vidaVillano -= heroe.ataque()
                            
                        

                    ganaono = heroe.GanaOPierde()
                    if ganaono == False:
                        break

                    villano.msg2()














#Else principal
            else:
#Codigo de la habilidad 1
                if habi == 1:
                    heroe.regenerar()
                    if heroe._rondaDaño > 0:
                        heroe._rondaDaño -= 1
                    
                        if habi2 == 1:
                            villano.roboVida()
                            print("El villano ha robado vida")
                            if villano._rondaEnvenenar > 0:
                                
                                villano._rondaEnvenenar -= 1  
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                


                            else:

                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() - heroe.calcularDañoReducido())


                            
            
                        
                        elif habi2 == 2:
                            print("El villano ha activado la habilidad de proteccion")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                                


                            else:
                                heroe._vidaHero -= (villano.ataque() - heroe.calcularDañoReducido())
                            
                            


                        
                        
                        elif habi2 == 3:
                            print("El villano ha activado la habilidad de envenenar")
                            villano.envenenarHero()
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                            




                        
                        
                        
                        elif habi2 == 4:
                            print("El villano ha activado la habilidad de aumentar el daño")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.DañoExtra() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                                


                            else:
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.DañoExtra()) - heroe.calcularDañoReducido())
                                
                            



                        
                        
                        elif habi2 == 5:
                            print("El villano ha activado la habilidad de super ataque")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                


                            else:
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.ataqueSuperFuerte()) - heroe.calcularDañoReducido())
                                
                                
                                



                        
                        
                        else:
                            
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                

                            else:

                                heroe._vidaHero -= villano.ataque() - heroe.calcularDañoReducido()
                                villano._vidaVillano -= heroe.ataque()
                                

                            
                        ganaono = heroe.GanaOPierde()
                        if ganaono == False:
                            break
                        
                        villano.msg2() 
                    



#Else de la habilidad 1
                    else:
                        if habi2 == 1:
                            villano.roboVida()
                            print("El villano ha robado vida")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1  
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                        

                            else:

                                
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= villano.ataque()

                        
                        elif habi2 == 2:
                            print("El villano ha activado la habilidad de proteccion")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                heroe._vidaHero -= villano.ataque()
                            
                            
                        
                        elif habi2 == 3:
                            print("El villano ha activado la habilidad de envenenar")
                            villano.envenenarHero()
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                            

                        
                        elif habi2 == 4:
                            print("El villano ha activado la habilidad de aumentar el daño")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.DañoExtra() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.DañoExtra())
                                
                            
                        
                        elif habi2 == 5:
                            print("El villano ha activado la habilidad de super ataque")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.ataqueSuperFuerte()) 
                                
                                
                                
                            
                        
                        else:
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                                

                            else:

                                heroe._vidaHero -= villano.ataque() 
                                villano._vidaVillano -= heroe.ataque()
                                
                            

                        ganaono = heroe.GanaOPierde()
                        if ganaono == False:
                            break

                        villano.msg2()
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        

#Codigo para la habilidad numero 2

                elif habi == 2:
                    if heroe._rondaDaño > 0:
                        heroe._rondaDaño -= 1


                    if habi2 == 1:
                            villano.roboVida()
                            print("El villano ha robado vida")
                            if villano._rondaEnvenenar > 0:
                                
                                villano._rondaEnvenenar -= 1  
                                villano._vidaVillano -= heroe.ataque()
                                
                                


                            else:

                                villano._vidaVillano -= heroe.ataque()


                            
            
                        
                    elif habi2 == 2:
                            print("El villano ha activado la habilidad de proteccion")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                            

                        
                        
                        
                        
                    elif habi2 == 3:
                            print("El villano ha activado la habilidad de envenenar")    
                            villano.envenenarHero()
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()




                        
                        
                        
                    elif habi2 == 4:
                            print("El villano ha activado la habilidad de aumentar el daño")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                              


                            else:
                                villano._vidaVillano -= heroe.ataque()
       
                            


                        
                        
                    elif habi2 == 5:
                            print("El villano ha activado la habilidad de super ataque")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
               

                            else:
                                villano._vidaVillano -= heroe.ataque()
                                                
                                


                        
                        
                    else:
                            
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
             

                            else:

                                villano._vidaVillano -= heroe.ataque()
                                
                            
                    ganaono = heroe.GanaOPierde()    
                    if ganaono == False:
                            break
                        
                    villano.msg2()



















#Codigo de la habilidad numero 3
                elif habi == 3:
                    heroe.ReducirDaño()
                    heroe._rondaDaño -= 1
                    
                    if habi2 == 1:
                        villano.roboVida()
                        print("El villano ha robado vida")
                        if villano._rondaEnvenenar > 0:
                            
                            villano._rondaEnvenenar -= 1  
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                            


                        else:

                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= (villano.ataque() - heroe.calcularDañoReducido())

                       


                        
        
                    
                    elif habi2 == 2:
                        print("El villano ha activado la habilidad de proteccion")
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                            


                        else:
                            heroe._vidaHero -= (villano.ataque() - heroe.calcularDañoReducido())
                        
                        

                    
                    
                    elif habi2 == 3:
                        print("El villano ha activado la habilidad de envenenar")
                        villano.envenenarHero()
                        villano._rondaEnvenenar -= 1
                        villano._vidaVillano -= heroe.ataque()
                        heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                        



                    
                    
                    
                    elif habi2 == 4:
                        print("El villano ha activado la habilidad de aumentar el daño")
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.DañoExtra() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                            


                        else:
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.DañoExtra()) - heroe.calcularDañoReducido())
                            
                        


                    
                    
                    elif habi2 == 5:
                        print("El villano ha activado la habilidad de super ataque")
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                            


                        else:
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.ataqueSuperFuerte()) - heroe.calcularDañoReducido())
                            
                            
                            


                    
                    
                    else:
                        
                        if villano._rondaEnvenenar > 0:
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                            

                        else:

                            heroe._vidaHero -= villano.ataque() - heroe.calcularDañoReducido()
                            villano._vidaVillano -= heroe.ataque()
                            
                        
                    ganaono = heroe.GanaOPierde()
                    if ganaono == False:
                        break
                    
                    villano.msg2()
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
#Codigo de la habilidad numero 4
                elif habi == 4:

                    if heroe._rondaDaño > 0:
                        heroe._rondaDaño -= 1
                        
                        if habi2 == 1:
                            villano.roboVida()
                            print("El villano ha robado vida")
                            if villano._rondaEnvenenar > 0:
                                
                                villano._rondaEnvenenar -= 1  
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                


                            else:

                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= (villano.ataque() - heroe.calcularDañoReducido())


                            
            
                        
                        elif habi2 == 2:
                            print("El villano ha activado la habilidad de proteccion")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                                


                            else:
                                heroe._vidaHero -= (villano.ataque() - heroe.calcularDañoReducido())
                            
                            

                        
                        
                        elif habi2 == 3:
                            
                            villano.envenenarHero()
                            print("El villano ha activado la habilidad de envenenar")
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                            heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                            



                        
                        
                        
                        elif habi2 == 4:
                            print("El villano ha activado la habilidad de aumentar el daño")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= ((villano.ataque() + villano.DañoExtra() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                                


                            else:
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= ((villano.ataque() + villano.DañoExtra()) - heroe.calcularDañoReducido())
                                
                            


                        
                        
                        elif habi2 == 5:
                            print("El villano ha activado la habilidad de super ataque")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= ((villano.ataque() + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                


                            else:
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= ((villano.ataque() + villano.ataqueSuperFuerte()) - heroe.calcularDañoReducido())
                                
                                
                                


                        
                        
                        else:
                            
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                

                            else:

                                heroe._vidaHero -= villano.ataque() - heroe.calcularDañoReducido()
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                
                            
                        ganaono = heroe.GanaOPierde()
                        if ganaono == False:
                            break
                        
                        villano.msg2() 
                
                
                
                
#Else de la opcion de habilidad 4 
                    else:

                        if habi2 == 1:
                            villano.roboVida()
                            print("El villano ha robado vida")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1  
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                        

                            else:

                                
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= villano.ataque()

                            
                        
                        elif habi2 == 2:
                            print("El villano ha activado la habilidad de proteccion")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                heroe._vidaHero -= villano.ataque()
                            
                            
                        
                        elif habi2 == 3:
                            print("El villano ha activado la habilidad de envenenar")
                            villano.envenenarHero()
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                            heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                            

                        
                        elif habi2 == 4:
                            print("El villano ha activado la habilidad de aumentar el daño")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= (villano.ataque() + villano.DañoExtra() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= (villano.ataque() + villano.DañoExtra())
                                
                            
                        
                        elif habi2 == 5:
                            print("El villano ha activado la habilidad de super ataque")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= (villano.ataque() + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= (villano.ataque() + villano.ataqueSuperFuerte()) 
                                
                                
                                
                            
                        
                        else:
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                                

                            else:

                                heroe._vidaHero -= villano.ataque() 
                                villano._vidaVillano -= (heroe.ataque() + heroe.DañoExtra())
                                
                            

                        ganaono = heroe.GanaOPierde()
                        if ganaono == False:
                            break

                        villano.msg2()



















#Codigo de habilida numero 5
                elif habi == 5:
                    if heroe._rondaDaño > 0:
                        heroe._rondaDaño -= 1

                        contra = heroe.ataque() 

                        if habi2 == 1:
                            villano.roboVida()
                            print("El villano ha robado vida")
                            if villano._rondaEnvenenar > 0:
                                
                                villano._rondaEnvenenar -= 1  
                                villano._vidaVillano -= contra * 2.5
                                heroe._vidaHero -= ((contra + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                


                            else:

                                villano._vidaVillano -= contra * 2.5
                                heroe._vidaHero -= (contra - heroe.calcularDañoReducido())

                            
            
                        
                        elif habi2 == 2:
                            print("El villano ha activado la habilidad de proteccion")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                heroe._vidaHero -= ((contra + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                                


                            else:
                                heroe._vidaHero -= (contra - heroe.calcularDañoReducido())
                            


                        
                        
                        elif habi2 == 3:
                            print("El villano ha activado la habilidad de envenenar")
                            villano.envenenarHero()
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= contra * 2.5
                            heroe._vidaHero -= ((contra + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                            

                        
                        
                        elif habi2 == 4:
                            print("El villano ha activado la habilidad de aumentar el daño")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= contra * 2.5
                                heroe._vidaHero -= ((contra + villano.DañoExtra() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                                


                            else:
                                villano._vidaVillano -= contra * 2.5
                                heroe._vidaHero -= ((contra + villano.DañoExtra()) - heroe.calcularDañoReducido())
                                
                            
                        
                        
                        elif habi2 == 5:
                            print("El villano ha activado la habilidad de super ataque")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= contra * 2.5
                                heroe._vidaHero -= ((contra + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                


                            else:
                                villano._vidaVillano -= contra * 2.5
                                heroe._vidaHero -= ((contra + villano.ataqueSuperFuerte()) - heroe.calcularDañoReducido())
                                



                        
                        
                        else:
                            
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= contra * 2.5
                                heroe._vidaHero -= ((contra + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                

                            else:

                                heroe._vidaHero -= contra - heroe.calcularDañoReducido()
                                villano._vidaVillano -= contra * 2.5
                                
                        
                        ganaono = villano.GanaOPierde()    
                        
                        if ganaono == False:
                            break
                        
                        villano.msg2()

                    





#Else de habilidad 5
                    else: #vbjbdjzbjhsdfjbjvhdbhbvhfbjhdfhjfdjbjfdbj
                        contra = heroe.ataque()
                        

                        if habi2 == 1:
                            villano.roboVida()
                            print("El villano ha robado vida")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1  
                                villano._vidaVillano -= contra * 2
                                heroe._vidaHero -= (contra + villano.calcularDañoPorEnvenenar())
                        

                            else:

                                
                                villano._vidaVillano -= contra * 2
                                heroe._vidaHero -= contra


                        
                        elif habi2 == 2:
                            print("El villano ha activado la habilidad de proteccion")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                heroe._vidaHero -= (contra + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                heroe._vidaHero -= contra
                            
                            

                        
                        elif habi2 == 3:
                            print("El villano ha activado la habilidad de envenenar")
                            villano.envenenarHero()
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= contra * 2
                            heroe._vidaHero -= (contra + villano.calcularDañoPorEnvenenar())
                            


                        
                        elif habi2 == 4:
                            print("El villano ha activado la habilidad de aumentar el daño")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= contra * 2
                                heroe._vidaHero -= (contra + villano.DañoExtra() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                villano._vidaVillano -= contra * 2
                                heroe._vidaHero -= (contra + villano.DañoExtra())
                                

                        
                        elif habi2 == 5:
                            print("El villano ha activado la habilidad de super ataque")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= contra * 2
                                heroe._vidaHero -= (contra + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                villano._vidaVillano -= contra * 2
                                heroe._vidaHero -= (contra + villano.ataqueSuperFuerte()) 
                                
                                
  
                            
                        
                        else:
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= contra * 2
                                heroe._vidaHero -= (contra + villano.calcularDañoPorEnvenenar())
                                

                            else:

                                heroe._vidaHero -= contra 
                                villano._vidaVillano -= contra * 2
                                
                        
                        
                        ganaono = villano.GanaOPierde()
                        
                        if ganaono == False:
                            break

                        villano.msg2()










#Codigo de la habilidad 6
                else:
                    
                    if heroe._rondaDaño > 0:
                        heroe._rondaDaño -= 1


                    
                        if habi2 == 1:
                            villano.roboVida()
                            print("El villano ha robado vida")
                            if villano._rondaEnvenenar > 0:
                                
                                villano._rondaEnvenenar -= 1  
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                


                            else:

                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() - heroe.calcularDañoReducido())

                            


            
                        
                        elif habi2 == 2:
                            print("El villano ha activado la habilidad de proteccion")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                                


                            else:
                                heroe._vidaHero -= (villano.ataque() - heroe.calcularDañoReducido())
                            


                        
                        
                        elif habi2 == 3:
                            print("El villano ha activado la habilidad de envenenar")
                            villano.envenenarHero()
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                            



                        
                        
                        
                        elif habi2 == 4:
                            print("El villano ha activado la habilidad de aumentar el daño")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.DañoExtra() + villano.calcularDañoPorEnvenenar()) - heroe.calcularDañoReducido())
                                


                            else:
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.DañoExtra()) - heroe.calcularDañoReducido())
                                
                            


                        
                        
                        elif habi2 == 5:
                            print("El villano ha activado la habilidad de super ataque")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                


                            else:
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.ataqueSuperFuerte()) - heroe.calcularDañoReducido())
                                
                                
                                


                        
                        
                        else:
                            
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= ((villano.ataque() + villano.calcularDañoPorEnvenenar())- heroe.calcularDañoReducido())
                                

                            else:

                                heroe._vidaHero -= villano.ataque() - heroe.calcularDañoReducido()
                                villano._vidaVillano -= heroe.ataque()
                                
                            
                        ganaono = heroe.GanaOPierde()
                        
                        if ganaono == False:
                            break
                        
                        villano.msg2()





#Else de la habilidad 6
                    else:


                        if habi2 == 1:
                            villano.roboVida()
                            print("El villano ha robado vida")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1  
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                        

                            else:

                                
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= villano.ataque()

                        
                        
                        elif habi2 == 2:
                            print("El villano ha activado la habilidad de proteccion")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                heroe._vidaHero -= villano.ataque()
                            
                            
                        
                        elif habi2 == 3:
                            print("El villano ha activado la habilidad de envenenar")
                            villano.envenenarHero()
                            villano._rondaEnvenenar -= 1
                            villano._vidaVillano -= heroe.ataque()
                            heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                            

                        
                        elif habi2 == 4:
                            print("El villano ha activado la habilidad de aumentar el daño")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.DañoExtra() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.DañoExtra())
                                
                            
                        
                        elif habi2 == 5:
                            print("El villano ha activado la habilidad de super ataque")
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.ataqueSuperFuerte() + villano.calcularDañoPorEnvenenar())
                                


                            else:
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.ataqueSuperFuerte()) 
                                
                                
                                
                            
                        
                        else:
                            if villano._rondaEnvenenar > 0:
                                villano._rondaEnvenenar -= 1
                                villano._vidaVillano -= heroe.ataque()
                                heroe._vidaHero -= (villano.ataque() + villano.calcularDañoPorEnvenenar())
                                

                            else:

                                heroe._vidaHero -= villano.ataque() 
                                villano._vidaVillano -= heroe.ataque()
                                
                            

                        ganaono = heroe.GanaOPierde()
                        if ganaono == False:
                            break

                        villano.msg2()

        
        
        
        break
