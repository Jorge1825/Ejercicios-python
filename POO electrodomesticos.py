""" 
4. Crearemos una supeclase llamada Electrodoméstico con las siguientes características:
 Sus atributos son precio base, color, consumo energético (letras entre A y F) y peso.
 Por defecto, el color será blanco, el consumo energético será F, el precioBase es de 100 € y el peso de 5 kg.
 Los colores disponibles son blanco, negro, rojo, azul y gris.
Los constructores que se implementaran serán
 Un constructor por defecto.
Los métodos que implementara serán:
 comprobarConsumoEnergetico: comprueba que la letra es correcta, sino es correcta usara la letra por defecto. Se invocara al crear el objeto.
 comprobarColor: comprueba que el color es correcto, sino lo es usa el color por defecto. Se invocara al crear el objeto
 precioFinal(): según el consumo energético, aumentara su precio, y según su tamaño, también. Esta es la lista de precios:
Crearemos una subclase llamada Lavadora con las siguientes características:
 Su atributo es carga, además de los atributos heredados.
 Por defecto, la carga es de 5 kg.
Los constructores que se implementaran serán:
 Un constructor por defecto.
Los métodos que se implementara serán:
 precioFinal(): si tiene una carga mayor de 30 kg, aumentara el precio 50 €, sino es así no se incrementara el precio. Llama al método padre y añade el código necesario. Recuerda que las condiciones que hemos visto en la clase Electrodoméstico también deben afectar al precio.
Crearemos una subclase llamada Televisión con las siguientes características:
 Sus atributos son resolución (en pulgadas) y sintonizador TDT (booleano), además de los atributos heredados.
 Por defecto, la resolución será de 20 pulgadas y el sintonizador será false.
Los constructores que se implementaran serán:
 Un constructor por defecto.
Los métodos que se implementara serán:
 precioFinal(): si tiene una resolución mayor de 40 pulgadas, se incrementara el precio un 30% y si tiene un sintonizador TDT incorporado, aumentara 50 €. Recuerda que las condiciones que hemos visto en la clase Electrodoméstico también deben afectar al precio.
Ahora crea un programa que realice lo siguiente:
 Crea un array de Electrodomésticos de 10 posiciones.
 Asigna a cada posición un objeto de las clases anteriores con los valores que desees.
 Ahora, recorre este array y ejecuta el método precioFinal().
 Deberás mostrar el precio de cada clase, es decir, el precio de todas las televisiones por un lado, el de las lavadoras por otro y la suma de los Electrodomésticos (puedes crear objetos Electrodoméstico, pero recuerda que Televisión y Lavadora también son electrodomésticos).
 Por ejemplo, si tenemos un Electrodoméstico con un precio final de 300, una lavadora de 200 y una televisión de 500, el resultado final será de 1000 (300+200+500) para electrodomésticos, 200 para lavadora y 500 para televisión.
"""




from os import system

class Electrodomestico:
    
    def comprobarConsumoEnergetico(self,consumo):
        consumo = consumo.upper()
        letras = "ABCDEF"
        
        if consumo in letras:
            return consumo
        
        else:
            return "F"
   
    def comprobarColor(self,color,coloresDisponibles):
        
        color = color.lower()
        color = color.capitalize()
        
        if color in coloresDisponibles:
            return color
        else:
            return "Blanco"
    
    
    
    def __init__(self,precio_base = 100, color = "Blanco", consumo_energetico = "F", peso = 5):
        
        self._coloresDisponibles = ["Blanco", "Rojo", "Azul","Negro","Gris"]
        self._color = self.comprobarColor(color,self._coloresDisponibles)
        self._consumo_energetico = self.comprobarConsumoEnergetico(consumo_energetico)
        self._peso = peso
        self._precio_base = precio_base
    
    
    def precioFinal(self):
 
        if self._consumo_energetico == "A":
            self._precio_base += 100
            
        elif self._consumo_energetico == "B":
            self._precio_base += 80
        
        elif self._consumo_energetico == "C":
            self._precio_base += 60
            
        elif self._consumo_energetico == "D":
            self._precio_base += 50
            
        elif self._consumo_energetico == "E":
            self._precio_base += 30
        
        else:
            self._precio_base += 10
            
            
        if self._peso >= 0 and self._peso <= 19:
            self._precio_base += 10
            
        elif self._peso >= 20 and self._peso <= 49:
            self._precio_base += 50
            
        elif self._peso >= 50 and self._peso <= 79:
            self._precio_base += 80
            
        elif self._peso >= 80:
            self._precio_base += 100
        
        
        return round(self._precio_base,2)
    
    
    
    
    
    
class Lavadora(Electrodomestico):
    
    def __init__(self,precio_base = 100, color = "Blanco", consumo_energetico = "F", peso = 5, carga = 5):
        super().__init__(precio_base, color, consumo_energetico, peso)
        self._carga = carga
    
    def precioFinal(self):

        if self._carga >= 30:
            self._precio_base += 50
            
        else:
            self._precio_base
            
        return super().precioFinal() #llama al metodo precioFinal de la clase padre
        



class Television(Electrodomestico):
    
    def __init__(self,precio_base = 100, color = "Blanco", consumo_energetico = "F", peso = 5, resolucion = 20, sintonizador = False):
        super().__init__(precio_base, color, consumo_energetico, peso)
        self._resolucion = resolucion
        self._sintonizador = sintonizador
    
    def precioFinal(self):
        
        if self._resolucion >= 40:
            self._precio_base += (self._precio_base * 0.3)
            
        if self._sintonizador == True:
            self._precio_base += 50
            
        return super().precioFinal() #llama al metodo precioFinal de la clase padre







def main():
    system("cls")
    opcion = 0
    
    print("Elija un tipo de electrodomestico:")
    print("1. Electrodomestico")
    print("2. Lavadora")
    print("3. Television")
    
    try:
        opcion = int(input("Ingrese una opcion: "))
    except:
        print("Ingrese una opcion valida")
        main()


    return opcion





def resultado():
    
    preFinalElectrodomestico = 0
    preFinalLavadora = 0
    preFinalTelevision = 0
    
    array = []
    for i in range(1,3):
        opcion = main()
        print(opcion)
        

    
        def opci():
            try:
                pBase = 0
                color = ""
                consumoEnergetico = ""
                peso = 0
                pBase = float(input("Ingrese el precio base: "))
                color= input("Ingrese el color: ")
                consumoEnergetico = input("Ingrese el consumo energetico: ")
                peso = float(input("Ingrese el peso: "))

                return pBase, color, consumoEnergetico, peso
            

            except:
                print("Valor invalido")
                opci()

        pBase,color,consumoEnergetico,peso =opci()
        
        if opcion == 1:
            
            i = Electrodomestico(pBase,color,consumoEnergetico,peso)
            array.append(i.precioFinal())
            preFinalElectrodomestico += i.precioFinal()
            
            
        elif opcion == 2:
            def opci2():
                try:
                    carga = float(input("Ingrese la carga: "))
                    return carga
                
                except:
                    print("Valor invalido")
                    opci2()
            carga = opci2()

            
            i = Lavadora(pBase,color,consumoEnergetico,peso,carga)   
            array.append(i.precioFinal())
            preFinalElectrodomestico += i.precioFinal()
            preFinalLavadora += i.precioFinal()
            
        
        
        else:
            def opci3():
                try:
                    resolucion = float(input("Ingrese la resolucion: "))
                    sintonizador = input("Tiene sintonizador, escriba si o no: ")
                    
                    if sintonizador == "si" or sintonizador == "Si" or sintonizador == "SI":
                        sintonizador = True
                    
                    return resolucion, sintonizador
                except:
                    print("Valor invalido")
                    opci3()   
                        
            resolucion,sintonizador = opci3()
            i = Television(pBase,color,consumoEnergetico,peso,resolucion,sintonizador) 
            array.append(i.precioFinal())
            preFinalElectrodomestico += i.precioFinal()
            preFinalTelevision += i.precioFinal()
            
    
    print("El precio final de los electrodomesticos es: €",sum(array),"\n El valor total de las lavadoras es: €", preFinalLavadora ,"\n El valor total de las televisiones es: €",preFinalTelevision)       
            
resultado()





""" c = Electrodomestico(100,"Azul","E",4)
print(c._color)
print(c._consumo_energetico)
print(c.precioFinal())


print("\n\n")
lava = Lavadora(100,"Rojo","E",4,32)
print(lava._color)

print(lava.precioFinal())

print("\n\n")

tv = Television(100,"Rojo","E",4,40,True)
print(tv._color)
print(tv.precioFinal()) """