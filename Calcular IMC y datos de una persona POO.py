""" Sus atributos son: nombre, edad, CC, sexo (H hombre, M mujer), peso y altura.
 Por defecto, todos los atributos menos el CC serán valores por defecto según su tipo (0 números, cadena vacía para String, etc.).
 Sexo será femenino por defecto.
 Un constructor con valores por defecto.
Los métodos que se implementaran son:
 calcularIMC(): calculara si la persona está en su peso ideal (peso en kg/(altura^2 en m)), si esta fórmula devuelve un valor menor que 20, la función devuelve un -1, si devuelve un número entre 20 y 25 (incluidos), significa que está por debajo de su peso ideal la función devuelve un 0 y si devuelve un valor mayor que 25 significa que tiene sobrepeso, la función devuelve un 1.
 esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano.
 toString(): devuelve toda la información (formateada en un texto) del objeto.
 generaCC(): genera un número aleatorio de 8 cifras, Este método será invocado cuando se construya el objeto.
Ahora, crea un programa que haga lo siguiente:
 Pide por teclado el nombre, la edad, sexo, peso y altura.
 Crea 3 objetos de la clase anterior, el primer objeto obtendrá las anteriores variables pedidas por teclado, el segundo objeto obtendrá todos los anteriores menos el peso y la altura y el último con los valores por defecto.
 Para cada objeto, deberá comprobar si está en su peso ideal, tiene sobrepeso o por debajo de su peso ideal con un mensaje.
 Indicar para cada objeto si es mayor de edad.
 Por último, mostrar la información de cada objeto. """


import random


class Persona:

    _cc = ""

    def generaCC(self):

        for i in range(1, 9):
            self._cc += str(random.randint(0, 9))
        return self._cc

    def __init__(self, nombre=str(""),  edad=int(0), sexo="Femenino", peso=float(0), altura=float(0)):
        self._nombre = nombre
        self._edad = edad
        self._sexo = sexo
        self._peso = peso
        self.cc = self.generaCC()
        self._altura = altura

    def calcularIMC(self):
        if self._peso == 0 or self._altura == 0:
            return 0

        if self._peso/(self._altura**2) < 20:
            return -1

        elif self._peso/(self._altura**2) >= 20 and self._peso/(self._altura**2) <= 25:

            return 0
        else:
            return 1

    def esMayorDeEdad(self):
        if self._edad >= 18:
            return True
        else:
            return False

    def toString(self):
        print("Nombre: " + self._nombre + "\nEdad: " + str(self._edad) + "\nCC: " + self._cc +
              "\nSexo: " + self._sexo + "\nPeso: " + str(self._peso) + "\nAltura: " + str(self._altura))


def main():
    nombre = input("Introduce tu nombre: ")

    edad = input("Introduce tu edad: ")
    if edad.isdigit():
        edad = int(edad)
    else:
        print("Error, introduce una edad valida")
        main()

    sexo = input("Introduce tu sexo: ")

    try:
        peso = float(input("Introduce tu peso: "))
        
    except:
        print("Error, introduce un peso valido")
        main()    

    try:
        altura = float(input("Introduce tu altura: "))
    except:
        print("Error, introduce una altura valida")
        main()
        
    return nombre, edad, sexo, peso, altura


nom, edad, sexo, peso, altura = main()


per = Persona(nom, edad, sexo, peso, altura)
per.toString()
per.generaCC()
if per.calcularIMC() == -1:
    print("La persona tiene el peso ideal")

elif per.calcularIMC() == 0:
    print("Está por debajo de su peso ideal")

elif per.calcularIMC() == 1:
    print("Tiene sobrepeso")


if per.esMayorDeEdad() == True:
    print("La persona es mayor de edad")
else:
    print("La persona no es mayor de edad")


print("\n\n")
Person = Persona(nom, edad, sexo)
Person.toString()
if Person.calcularIMC() == -1:
    print("La persona tiene el peso ideal")

elif Person.calcularIMC() == 0:
    print("Está por debajo de su peso ideal")

elif Person.calcularIMC() == 1:
    print("Tiene sobrepeso")


if Person.esMayorDeEdad() == True:
    print("La persona es mayor de edad")
else:
    print("La persona no es mayor de edad")


print("\n\n")
Persona = Persona()
Persona.toString()
if Persona.calcularIMC() == -1:
    print("La persona tiene el peso ideal")

elif Persona.calcularIMC() == 0:
    print("Está por debajo de su peso ideal")

elif Persona.calcularIMC() == 1:
    print("Tiene sobrepeso")


if Persona.esMayorDeEdad() == True:
    print("La persona es mayor de edad")
else:
    print("La persona no es mayor de edad")
