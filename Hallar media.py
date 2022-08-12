acu = 0
con = 0
while True:
    
    
    print("-----------------------------------------------\n")
    numeros = input("Digite un numeros, si desea terminar escriba 0, si desea salir escriba 'salir'\n")
    
    if numeros == "Salir" or numeros == "salir" or numeros == "SALIR":
        break
    
    numeros = float(numeros)
    acu += numeros
    

    if numeros == 0:
        
        def media(acu,con):
            return acu/con
    
    else:
        con += 1
        continue
    
    print("La media de los numeros ingresados es:", round(media(acu,con),1))
    acu = 0
    con = 0

