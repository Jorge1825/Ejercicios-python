while True:
    print("-----------------------------------------------\n")
    n = list (map(int, input("Digite una lista de numeros separados por espacios (1 2 3), si desea salir escriba 0\n").split()))
    
    if n == [0]:
        break
    else:
    
        def square(n):
            """Función que calcula los cuadrados de una lista de números.
            Parámetros
            sample: Es una lista de números
            Devuelve una lista con los cuadrados de los números de la lista sample.
            """
            list = []
            for i in n:
                list.append(i**2)
            return list

        def statistics(sample):
            """Función que calcula la media, varianza y desviación típica de una muestra de números.
            Parámetros
            sample: Es una lista de números
            Devuelve un diccionario con la media, varianza y desviación típica de los números en sample.
            """

            stat1 = sum(sample)/len(sample)
            stat2 = sum(square(sample))/len(sample)-stat1 **2
            stat3 = stat2**0.5
            
            return print(f"La media de los numeros ingresados es: {stat1}, la varianza es: {stat2}, y la desviación {stat3}")

    statistics(n)
