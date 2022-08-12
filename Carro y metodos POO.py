#Ejercicio del profesor

class Coche: 
    marca = '' 
    modelo = '' 
    color = '' 
    numero_de_puertas = 0 
    cuenta_kilometros = 0 
    velocidad = 0 
    arrancado = False
    
    def arrancar(self): 
        if not self.arrancado: 
            print('Roarrrr') 
            self.arrancado = True 
        else: 
            # Dale al encendido estando el coche arrancado y escucha... 
            print('Kriiiiiiiiiiicccc') 
    
    def parar(self): 
        self.arrancado = False 
        
    def acelerar(self): 
        if self.arrancado: 
            self.velocidad = self.velocidad + 1 
    
    def frenar(self): 
        if self.velocidad > 0: 
            self.velocidad = self.velocidad - 1 
    
    
    def pitar(self): 
        print('Bip Bip Bip') 
    
    def consultar_velocimetro(self): 
        return self.velocidad 
    
    def consultar_cuenta_kilometros(self): 
        
        return self.cuenta_kilometros
    
    
    
    
    
    
    
    
    
class Persona: 
    sexo = '' 
    nombre = '' 
    edad = 0 
    coche = Coche() # El coche que conduce esa persona
    
    
    def saludar(self): 
        print('Hola, me llamo', self.nombre) 
    
    def dormir(self): 
        print('Zzzzzzzzzzz') 
    
    def obtener_edad(self):
        return self.edad
    
    
    
    
    
    
    
    
    
    
coche1 = Coche()
coche2 = Coche()

print(id(coche1))
print(id(coche2))




coche1.marca = "Seat" 
coche1.modelo = "León" 
coche1.color = "negro"

coche2.marca = "Ford" 
coche2.modelo = "Fiesta" 
coche2.numero_de_puertas = 3


print(coche1.marca)
print(coche1.modelo)
print(coche1.color)
print(coche1.numero_de_puertas)
print(coche1.cuenta_kilometros)
print(coche1.velocidad)
print(coche1.arrancado)
coche1.arrancar()
print(coche1.arrancado)
print(coche2.arrancado)
coche1.arrancar()


coche1.acelerar()
print(coche1.velocidad)
coche1.acelerar()
print(coche1.velocidad)


coche1.frenar()
coche1.frenar() # Al tener velocidad 2 aplicamos dos veces el método
print(coche1.velocidad)

coche1.parar()
print(coche1.arrancado)
