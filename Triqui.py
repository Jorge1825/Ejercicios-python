
import math
import os


class triqui:
    def __init__(self):
        self.tablero = ["-" for i in range(9)]

        def elec():
            while True:
                self.MarcaJugador = input("Ingrese el simbolo que desea utilizar (X-O): ")
                os.system("cls")
                if self.MarcaJugador.upper() == "X" or self.MarcaJugador.upper() == "O":

                    if self.MarcaJugador.upper() == "X":
                        self.MarcaMaquina = "O"
                    else:
                        self.MarcaMaquina = "X"

                    break
                else:
                    print("Ingrese un simbolo valido")
                    continue

            return self.MarcaJugador.upper(), self.MarcaMaquina.upper()

        self.LetraJugador, self.LetraMaquina = elec()


    def MostrarTablero(self):
            print("\n")
            for i in range(3):
                print(" ", self.tablero[0+(i*3)], "|",
                      self.tablero[1+(i*3)], "|", self.tablero[2+(i*3)])

            print("\n")

    def TableroVacio(self, estado):
            return not "-" in estado

    def JuegoGana(self, estado, Letrajugador):

            if estado[0] == estado[1] == estado[2] == Letrajugador:
                return True
            if estado[3] == estado[4] == estado[5] == Letrajugador:
                return True
            if estado[6] == estado[7] == estado[8] == Letrajugador:
                return True
            if estado[0] == estado[3] == estado[6] == Letrajugador:
                return True
            if estado[1] == estado[4] == estado[7] == Letrajugador:
                return True
            if estado[2] == estado[5] == estado[8] == Letrajugador:
                return True
            if estado[0] == estado[4] == estado[8] == Letrajugador:
                return True
            if estado[2] == estado[4] == estado[6] == Letrajugador:
                return True

            return False

    def JuegoGanador(self):
            if self.JuegoGana(self.tablero, self.LetraJugador):
                os.system("cls")
                print("El jugador gana")

                return True

            if self.JuegoGana(self.tablero, self.LetraMaquina):
                os.system("cls")
                print("La maquina gana")

                return True

            if self.TableroVacio(self.tablero):
                os.system("cls")
                print("Empate")

                return True

            return False

    def iniciarJuego(self):
            JugadorHuma = JugadorHumano(self.LetraJugador)

            while True:
                print("Es el turno del jugador")
                self.MostrarTablero()

                jugada = JugadorHuma.movimiento(self.tablero)
                self.tablero[jugada] = self.LetraJugador
                if(self.JuegoGanador()):
                    break


class JugadorHumano:
    def __init__(self, letra):
        self.letra = letra

    def movimiento(self, estado):
        while True:
            try:
                movimiento = int(input("Ingrese el numero de la casilla(1-9) "))
                print()
                if estado[movimiento-1] == "-":
                    break
                else:
                    print("La casilla ya esta ocupada")
                    continue
            except:
                print("Ingrese un numero valido")
                continue

        return movimiento-1




#Usar Intelegencia Artifical

class Computadora(triqui):
    

    def jugadores(self,estado):
        n = len(estado)
        x = 0
        o = 0

        for i in range(9):
            if(estado[i] == "X"):
                x += 1
            if(estado[i] == "O"):
                o += 1
                
        return self.LetraJugador if x == o else self.LetraMaquina


    def PosVacias(self, estado):
        return [i for i, x in enumerate(estado) if x == "-"]  #Funcion que devuelve las posiciones vacias del tablero
    
    
    def TableMovimientos(self, estado, Vacias):
        nuevoEstado = estado.copy()
        Jugador = self.jugadores(estado)
        nuevoEstado[Vacias] - Jugador
        return nuevoEstado
        
        
    def Validar(self,estado):
        if(self.JuegoGana(estado,self.LetraJugador)):
            return True
        if(self.JuegoGana(estado,self.LetraMaquina)):
            return True
        
        return False

Triqui = triqui()
Triqui.iniciarJuego()
