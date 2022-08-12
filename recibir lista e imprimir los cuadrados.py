

while True:
    print("-----------------------------------------------\n")
    numeros = list (map(int, input("Digite una lista de numeros separados por espacios (1 2 3), si desea salir escriba 0\n").split()))
    
    if numeros == [0]:
        break
    else:
        def cua(numeros):
            for i in numeros:
                print(f"El cuadrado de {i} es: {i **2}")
                
            return 
        
    cua(numeros)

   
   
