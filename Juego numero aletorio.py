import random

numerojugadores = int(input("Ingrese la cantidad de jugadores "))
valor = 1000

def jugar(nombre):
    aletorio = random.randint(1,100)

    print(aletorio)
    intentos = 0
    while True:
        intentos += 1
        num = int(input("Por favor ingrese un numero entre el rango 1 y 100 "))
        
        if num < aletorio:
            print("El numero digitado es menor al calculado ")
            continue
        elif num > aletorio:
            print("El numero digitado es mayor al calculado ")
            continue
        else:
            print(f"Felicitaciones {nombre} acabas de acertar el numero con {intentos} intentos")
            break
    return intentos
    
    
for i in range (1, numerojugadores +1):
    Nombre = str(input(f"Ingrese el nombre del jugador {i}: "))
    r = jugar(Nombre)
       
    if r > valor:
        continue 
    if r < valor:
        valor =  r
        nom = Nombre
 
print(f"El ganador del juego es {nom} con {valor} intentos")
        
    