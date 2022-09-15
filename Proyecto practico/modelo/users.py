
import modelo.conection as conexion 
from datetime import datetime


try:

    conec = conexion.conecction()
    database = conec[0]
    cursor = conec[1]
except:
    input("presione enter para continuar")


class User():
    
    def __init__(self, nombre = str("NULL"), apellidos=str("NULL"), email =str("NULL"), password = str("NULL")):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
        
    def registrar(self):  
        cursor.execute("INSERT INTO users VALUES (null, %s, %s, %s, %s,%s)", (self.nombre, self.apellidos, self.email, self.password,datetime.now().date()))
        database.commit()
        if self.nombre == "NULL":
            print(f"Perfecto, te has registrado con el correo: {self.email}")  
        else:
            print(f"Perfecto {self.nombre} te has registrado con el correo: {self.email}")
        
        
        
    
    def validar(self):
        cursor.execute("select count(*) from users where Email = %s", (self.email,))
        unregistro = cursor.fetchone()
        if unregistro[0] != 0:
            print("El usuario ya existe")
            return True
        
        self.registrar()
        
        
    
    def validarLogin(self, email, password):
        cursor.execute("select Nombre from users where Email = %s and Password = %s", (email, password))
        unregistro = cursor.fetchone()
        if unregistro != None:
            print("Bienvenido {}, te has identificado en el sistema el {}".format(unregistro[0], datetime.now().date()))
            return unregistro[0]
        else:
            print("Usuario o contraseña incorrectos, por favor intenta de nuevo")
            return False
        



    def validarPass(self,email, password=str("NULL")):
        cursor.execute("select Password from users where Email = %s and Password = %s", (email, password))
        password2 = cursor.fetchone()
        print(password2)
        print(password)
        try:
            if password2[0] == password:
                return True
            
            print("Contraseña incorrecta, abortando operacion...")
            
            return False
        except:
            print("Contraseña incorrecta, abortando operacion...")
            
            return False

     

    def cambiarPassword(self, email, newpassword):
        cursor.execute("UPDATE users SET Password = %s WHERE Email = %s", (newpassword, email))
        database.commit()
        print("Perfecto, tu contraseña ha sido cambiada")
        
     
     
    def ConsultarPass(self):
        try:
            cursor.execute("select Password from users where Email = %s", (self.email,))
            password = cursor.fetchone()
            return password[0]
        except:
            print("Error, Posiblemente el correo no este registrado")
            return False


