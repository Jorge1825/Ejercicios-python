while True:
    print("-----------------------------------------------\n")
    n = int(input("ingrese el numero limite del que desea imprimir los numeros pares\n"))
    
    def par(n):
        for i in range(2, n+1,2):
            print(i)
    par(n)