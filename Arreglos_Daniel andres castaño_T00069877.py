print("\n\n*************************************")
print("**UNIVERRSIDAD TECNOLÓGICA DE BOLIVAR*")
print("*by: Daniel andres castaño. T00069877*")
print("**************************************\n\n")



n = int(input("Digite cantidad de estudiantes: "))      # Se pide al usuario la cantidad de alumnos a los que le desea obtener el codigo y la nota,  el numero se define como entero.

codigo = []         #
nota =[]            #
resultados=[]       #
contAp= 0           #
contRp = 0          # Aqui se inicializan variables dandole valores iniciales para el correcto funcionamiento, además se definen las listas a utilizar y los contadores que se utilizarán más adelante
mbien = 0           #
bien = 0            #
suficiente = 0      #
insuficiente = 0    #
mejornotalista = [] #
cont = -1           #

for x in range(0,n):                    # este ciclo se va a repetir según la cantidad de alumnos que haya ingresado inicialmente, con el fin de preguntar el codigo y la nota de cada alumno
    codigo.append(input("Introduce el codigo del estudiante:  "))                       # aqui preguntará al usuario el codigo del estudiante y gracias al metodo append agregará esa información a una lista la cual se usará más adelante
    nota.append(float(input("Introduce la nota del estudiante:  ")))                    # aqui preguntará al usuario la nota del estudiante que anteriormente registro y gracias al metodo append agregará esa información a una lista la cual se usará más adelante
     
mayor= max(nota)                         #La variable mayor almacenrá el valor maximo o más grande de la lista llamada nota, en la cual se encuentran todas las notas de los estudiantes que anteriormente se ingresaron. La funcion max automaticamente calculará el valor más grande de la lista.
menor= min(nota)                         #La variable menor almacenrá el valor minimo o más pequeño de la lista llamada nota, en la cual se encuentran todas las notas de los estudiantes que anteriormente se ingresaron. La funcion mim automaticamente calculará el valor más pequeño de la lista.
promedio=(sum(nota))/n                   #La variable promedio almacenrá el valor que se obtenga de sumar todas las notas y dividirlas entre la cantidad de las mismas, la función sum sumará automaticamente cada elemento que se encuentre en la lista notas.


print("\n-------La mayor y menor nota en todo el curso:-------")          #Mensaje en pantalla para indicar que los siguientes resultados son la nota mas grande entre todas las ingresadas y la nota minima entre las ingresadas.
print(f"\tmayor: {mayor}       menor: {menor}\t")                         #Imprimir mensaje indicando la nota mayor y la menor

print("\n-------Nota promedio del curso-------")            #Mensaje en pantalla para indicar que el siguiente resultado es el promedio total del curso.
print(f"\tPromedio:  {round(promedio,2)}  \n")              #Imprimir mensaje en pantalla en el que envie la palabra promedio y automaticamente envie el dato que almacena la variable promedio, y gracias a la función round() nos aseguramos que solo haya una parte entera y despues del punto un solo digito decimal.

for i in nota:                #Bucle que servira para evaluar cada nota que se encuentre entre la lista nota, de esa forma calcular cuantas personas aprobaron o reprobaron.
    if i <3.0:                #Condicion para evaluar si la nota es suficiente para reprovar.
        contRp +=1            #Contador de la cantidad de personas que van reprovando.
        
    else:
        contAp +=1             #Contador de la cantidad de personas que van aprovando.

print("-------Cantidad de estudiantes que aprobaron y reprobaron en el curso-------")           #Mensaje en pantalla para indicar que el siguiente resultado es la cantidad de alumnos que aprobaron y que reprobaron.
print(f"\taprobaron: {contAp}          reprobaron: {contRp}  \n")                                #Imprimir mensaje en pantalla en el que envie los valores de los contadores contAp y contRp los cuales almacenan la cantidad de alumnos reprobados y aprobados .

for t in nota:                  #Bucle que servira para evaluar cada nota que se encuentre entre la lista nota, de esa forma calcular el mensaje a lanzar por la nota obtenida y contar la cantidad de alumnos que obtienen un cierto rango de calificación.
    cont += 1                   #Contador que servira más adelante para establecer la posicion en la que se encuentra el alumno con mejor nota dentro de la lista "nota"
    
    if t >=4.0 and t <=5.0:     #Condicional para evaluar si la nota de un alumno está entre la categoria "Muy bien".
        resu = "Muy bien"       #En caso de cumplirse la condición anterior, generar un mensaje que se debe almacenar en una variable con el fin de extraerlo nuevamente más adelante.
        mbien += 1              #Contador de la cantida de alumnos que tienen una nota entre esa categoria.
    
    elif t >=3.0 and t <4.0:    #Condicional para evaluar si la nota de un alumno está entre la categoria "bien".
        resu = "Bien"           #En caso de cumplirse la condición anterior, generar un mensaje que se debe almacenar en una variable con el fin de extraerlo nuevamente más adelante.
        bien += 1               #Contador de la cantida de alumnos que tienen una nota entre esa categoria.
        
    elif t >=2.0 and t < 3.0:   #Condicional para evaluar si la nota de un alumno está entre la categoria "suficiente".
        resu = "suficiente"     #En caso de cumplirse la condición anterior, generar un mensaje que se debe almacenar en una variable con el fin de extraerlo nuevamente más adelante.
        suficiente +=1          #Contador de la cantida de alumnos que tienen una nota entre esa categoria.
        
    elif t >=0.5 and t < 52.0:  #Condicional para evaluar si la nota de un alumno está entre la categoria "insuficiente".
        resu = "insuficiente"   #En caso de cumplirse la condición anterior, generar un mensaje que se debe almacenar en una variable con el fin de extraerlo nuevamente más adelante.
        insuficiente +=1        #Contador de la cantida de alumnos que tienen una nota entre esa categoria.
        
    resultados.append(resu)     #Almacenar en una lista cada elemento que vaya obteniendo la varible resu, con el fin de imprimir más adelante los resultados obtenidos por el ciclo for.
    
    if t == mayor:              #Condicional para evaluar si la nota que actualmente está pasando por el bucle es la mayor.
        mejornotalista.append((codigo[cont]))  #En caso de cumplirse la condición anterior almacenar en una lista el codigo del estudiante al cual le pertenece la nota evaluada con anterioridad.
    

print("\t\n-------Tabla notas de los estudiantes-------\n")              #Mensaje en pantalla para mostrar el titulo de la tabla.
print("codigo \t | \t nota\t | \t\n")                                    #Mensaje en pantalla para mostrar el titulo de cada columna con el fin de mejorar la visualización de la información.

for codigo, nota , resultados in zip(codigo, nota, resultados):          #Ciclo para tomar cada objeto iterable de las listas codigo, nota y resultados, para ello se utilizó la función zip().
    print("-------------------------------------------")                 #Mensaje separador de linea
    print('{} \t | \t {} \t | \t {}'.format(codigo, nota, resultados))   #Impresion donde de le indica el formato a seguir por el interprete para evitar la aparición de corchetes y comas propios de los datos de una lista, además se imprimen los resultados de cada iteración del bucle con el fin de mostrar en pantalla el codigo, la nota y el mensaje de resultado que le pertenece a cada estudiante.
 
print("\n\n----------Categorias de resultados----------")                       #Mensaje en pantalla para indicar que el siguiente resultado es la cantidad de alumnos que tienen un resultado dentro de una de las categorias especificadas en el documento (Muy bien, Bien, suficiente e insuficiente).
print(f"\nEstudiantes que obtuvieron una nota Muy bien  {mbien} ")              #Mensaje en pantalla para mostrar la cantidad de alumnos que tienen la nota en el categoria "Muy bien".
print(f"Estudiantes que obtuvieron una nota bien  {bien} ")                     #Mensaje en pantalla para mostrar la cantidad de alumnos que tienen la nota en el categoria "Bien".
print(f"Estudiantes que obtuvieron una nota suficiente  {suficiente} ")         #Mensaje en pantalla para mostrar la cantidad de alumnos que tienen la nota en el categoria "suficiente".
print(f"Estudiantes que obtuvieron una nota insuficiente  {insuficiente} \n")   #Mensaje en pantalla para mostrar la cantidad de alumnos que tienen la nota en el categoria "insuficiente".

print("-------Porcentaje de estudiantes que aprobaron y reprobaron en el curso-------")      #Mensaje en pantalla para indicar que el siguiente resultado es el porcentaje de alumnos que aprobaron y reprobaron.
print(f"\taprobados: {round((contAp*100)/n,1)}   porciento")                                 #Mensaje en pantalla para mostrar el porcentaje de alumnos que aprobaron, utlizando una regla de tres para calcular dicho porcentaje e indicando con el metodo round() la cantidad de decimales que debe mostrar el resultado.
print(f"\treprobados: {round((contRp*100)/n,1)}    porciento\n")                             #Mensaje en pantalla para mostrar el porcentaje de alumnos que reprobaron, utlizando una regla de tres para calcular dicho porcentaje e indicando con el metodo round() la cantidad de decimales que debe mostrar el resultado.

print("-------Estudiantes que obtuvieron la más alta nota:-------")              #Mensaje en pantalla para indicar que el siguiente resultado es para mostrar el codigo del o de los estudiantes que obtuvieron la mejor nota.
print(' \t\n'.join(mejornotalista))                                              #Usando la función join, podemos obtener la cadena de caracteres limpia sin comas o corchetes e imprimir dichos caracteres de forma vertical.