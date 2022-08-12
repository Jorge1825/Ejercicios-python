while True:
    print("-----------------------------------------------\n")
    n = input("Ingrese un numero entero y que sea positivo\n")
    if '.' in n:
        print("El numero seguramente es decimal, por favor digite un numero entero")
        continue
    elif n == "":
        break
    else:
            def fact(n):
                n = int(n)
                acu=1
                for i in range(1,n+1):
                
                    if i == n: 
                        print(i, end = " = ")
                    else:
                        print(i, end = " * ")
                    
                    acu*=i
                return acu
    

    print(fact(n))
    continue
        