while True:
    print("-----------------------------------------------\n")
    r = float(input("Ingrese el radio del circulo\n"))
    if r == 0:
        break
    v = float(input("Ingrese la altura del cilindro\n"))
    if v == 0:
        break
    else:
        def circulo(r):
            return round(3.1426 * (r**2),2)
        
        def cilindro(v):
            return round(circulo(r) * v,2)

    print("El area del circulo es:", circulo(r))
    print("El volumen del cilindro es:", cilindro(v))
    continue