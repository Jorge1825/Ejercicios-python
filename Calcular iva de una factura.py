while True:
    print("-----------------------------------------------\n")
    n = float(input("Ingrese el valor de la factura sin iva\n"))
    if n == 0:
        break
    
    else:
        
        iva = input("Ingrese el numero del iva que desea aplicar, ejemplo '19'\n")
        def fact(n,iva):
                if iva == "":
                    vt = n * 21/100
                else: 
                    iva = float(iva)
                    vt = n * iva/100
                
                return round(vt,2)

    print("El valor total a pagar es: ", fact(n,iva))
    continue