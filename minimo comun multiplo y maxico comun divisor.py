while True:
    print("-----------------------------------------------\n")
    n1=int(input("Ingrese un numero entero, en caso de que desee salir escriba 0 \n"))
    if n1== 0:
        break
    n2=int(input("Ingrese un numero entero, en caso de que desee salir escriba 0 \n"))
    
    def mcm(x,y):
        n = max(x,y)
        
        while True:
            if (n % x == 0) and (n % y == 0):
                return n
            n += 1
            
            
    def mcd(x,y):
        defecto = 1
        
        if x % y ==0: 
            
            return y
        
        for k in range(int(y/2),0,-1):
            if x % k ==0 and y % k ==0:
                defecto = k
                break
        return defecto
            
    print(f"El mcm de {n1} y {n2} es ",mcm(n1,n2))
    print(f"El mcd de {n1} y {n2} es ",mcd(n1,n2))
