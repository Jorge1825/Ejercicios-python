

cadena = input("Ingrese la cadena de caracteres que desea invertir\n")

'''
metodo uno
for i in range(len(cadena)-1,-1,-1):
    print(cadena[i],end="")
'''
#Metodo dos y mas sencillo
print(cadena[::-1])