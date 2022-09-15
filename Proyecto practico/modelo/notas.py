
import modelo.conection as conexion 
from datetime import datetime

try:
    conec = conexion.conecction()
    database = conec[0]
    cursor = conec[1]
except:
    input("presione enter para continuar")


class Nota():
    def buscarIdUsuario(self,email):
        cursor.execute("select id from users where Email = %s", (email,))
        unregistro = cursor.fetchone()
        return unregistro[0]
        
        
    
    def __init__(self,usuario = str("NULL"),titulo = str("NULL"),descripcion = str("NULL")):
        self.usuario = usuario
        self.titulo = titulo
        self.descripcion = descripcion

        
        
    def validarTitulo(self,titulo2):
        cursor.execute("select count(*) from notas where Titulo = %s and Usuario_id = %s", (titulo2,self.buscarIdUsuario(self.usuario)))
        unregistro = cursor.fetchone()
        if unregistro[0] != 0:
            print("El titulo elegido ya esta en uso, por favor elige otro")
            input("Pulsa enter para continuar")
            
            return True
        
        
    def crearNota(self):
        idUser = self.buscarIdUsuario(self.usuario)
        
        cursor.execute("INSERT INTO notas VALUES (null, %s, %s, %s, %s)", (idUser, self.titulo, self.descripcion, datetime.now().date()))
        database.commit()
        print("Perfecto has creado la nota: {}".format(self.titulo))
        input("Pulsa enter para continuar")
        
    
    def MostrarNotas(self):
        idUser = self.buscarIdUsuario(self.usuario)
        cursor.execute("select count(*) from notas where Usuario_id = %s", (idUser,))
        count = cursor.fetchone()
        
        if count[0] == 0:
            print("\n****************************************************")
            print("No tienes notas creadas")
            print("\n****************************************************")
            input("Pulsa enter para continuar")
        
        else:
        
            cursor.execute("select Titulo,Descripcion from notas where Usuario_id = %s", (idUser,))
            unregistro = cursor.fetchall()
            for nota in unregistro:
                print("\n****************************************************")
                print("Titulo: {}".format(nota[0]))
                print("Descripcion: {}".format(nota[1]))
                print("****************************************************")
                
        
        
        
        
    def EliminarNotas(self,Delete):
        idUser = self.buscarIdUsuario(self.usuario)
        
        cursor.execute("delete from notas where Titulo = %s and Usuario_id = %s", (Delete,idUser))
        elementosAfectados = cursor.rowcount
        database.commit()
        
        if elementosAfectados == 0:
            print("No se ha podido eliminar la nota, verifique que el titulo sea correcto o que la nota exista")
            input("Pulsa enter para continuar")
            
        else:
            print("Perfecto has eliminado la nota: {}".format(Delete))
            input("Pulsa enter para continuar")
            
            
            
            
    def existenciaNota(self,titulo):
        idUser = self.buscarIdUsuario(self.usuario)
        cursor.execute("select count(*) from notas where Titulo = %s and Usuario_id = %s", (titulo,idUser))
        unregistro = cursor.fetchone()
        if unregistro[0] == 0:
            print("No existe la nota, verifique que el titulo sea correcto o que la nota exista")
            input("Pulsa enter para continuar")
            
        else:
            print("\nPerfecto la nota existe")
            cursor.execute("select Titulo,Descripcion from notas where Titulo = %s and Usuario_id = %s", (titulo,idUser))
            unregistro = cursor.fetchall()
            
            for nota in unregistro:
                print("\n****************************************************")
                print("Titulo: {}".format(nota[0]))
                print("Descripcion: {}".format(nota[1]))
                print("****************************************************")

            
            return True
        
    

    def modificarNota(self,antiguotitle,titulo,Ncambio,descripcion = str("NULL")):
        idUser = self.buscarIdUsuario(self.usuario)

        #Solo cambiar o modificar el titulo
        if Ncambio =="1":
            cursor.execute("update notas set Titulo = %s where Usuario_id = %s and Titulo = %s", (titulo,idUser,antiguotitle))
            database.commit()
            print("Perfecto has modificado el titulo de la nota: {} por {}".format(antiguotitle,titulo))
            input("Pulsa enter para continuar")
            
        #Solo cambiar o modificar la descripcion
        elif Ncambio =="2":
            cursor.execute("update notas set Descripcion = %s where Usuario_id = %s and Titulo = %s", (descripcion,idUser,antiguotitle))
            database.commit()
            print("Perfecto has modificado el contenido de la nota: {}".format(antiguotitle))
            input("Pulsa enter para continuar")
        
        #Cambiar o modificar el titulo y la descripcion
        
        else:
            cursor.execute("update notas set Titulo = %s, Descripcion = %s where Usuario_id = %s and Titulo = %s", (titulo,descripcion,idUser,antiguotitle))
            database.commit()
            print("Perfecto has modificado el titulo y el contenido de la nota}")
            input("Pulsa enter para continuar")
            
            
            
        
        
