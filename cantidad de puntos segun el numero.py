while True:
    print("\n-----------------------------------------------\n")
    numeros = list (map(int, input('Digite seis números: ').split()))

    
    def histograma(numeros):

        for e in numeros:
            print("")
            for i in range(1,e+1):
                print(i, end=' ')
        
        
    histograma(numeros)
    
    
'''''
def crear_histograma(lista, caracter='*'):
    for e in lista:
        print(caracter * e)
    lista = [2, 1, 5, 3]
    print(crear_histograma (lista)) 
'''