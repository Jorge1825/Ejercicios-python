""" Que tenga los atributos longitud y contraseña. Por defecto, la longitud será de 8.
Los constructores serán los siguientes:
 Un constructor con la longitud que nosotros le pasemos. Generará una contraseña aleatoria con esa longitud.
Los métodos que implementa serán:
 esFuerte(): devuelve un booleano si es fuerte o no, para que sea fuerte debe tener más de 2 mayúsculas, más de 1 minúscula y más de 5 números.
 generarPassword(): genera la contraseña del objeto con la longitud que tenga.
Ahora, crea un programa que:
 Crea un array de Passwords con el tamaño que tu le indiques por teclado.
 Crea un bucle que cree un objeto para cada posición del array.
 Indica también por teclado la longitud de los Passwords (antes de bucle).
 Crea otro array de booleanos donde se almacene si el password del array de Password es o no fuerte (usa el bucle anterior).
 Al final, muestra la contraseña y si es o no fuerte (usa el bucle anterior). Usa este simple formato:
contraseña1 valor_booleano1
contraseña2 valor_bololeano2 """


import random
class Password:


    def generarPassword(self):
        self._caracter = "QWERTYUIOPASDFGHJKLÑZXCVBNMqweretyuiopasdfghjklñzxcvbnm1234567890"
        self._pass = ""
        for i in range(1,self._longitud+1):
            self._pass += random.choice(self._caracter)
        return self._pass
    
    def __init__(self,longitud = 8) -> None:
        self._longitud = longitud
        self._contraseña = self.generarPassword()
        self._Fuerza = self.esFuerte()
    
    def esFuerte(self):
        
        mayus = 0
        minus = 0
        numero = 0

        for i in self._contraseña:
            if i.isupper():
                mayus += 1
            elif i.islower():
                minus += 1
            elif i.isdigit():
                numero += 1
        
        if mayus > 2 and minus > 0 and numero > 4:
            return True
        else:
            return False
        


def main():
    
    array = []
    bol = []
    cantidad = 0
    lon = 0
    try:
        cantidad = int(input("Ingrese la cantidad de contraseñas: "))
        lon = int(input("Ingrese la longitud de las contraseñas: "))
    except:
        print("Error, ingrese un numero")
        main()

    for i in range(1,cantidad+1):
        c = Password(lon)
        array.append(c._contraseña)
        bol.append(c._Fuerza)


    for i,j in zip(array,bol):
        
        if j == True:
            print(i,"Fuerte")
        else:
            print(i,"No fuerte")

    
main()


