import mysql.connector


def conecction():
    
    try:
        database = mysql.connector.connect(host="localhost", user="root", passwd="", db="mynote")
        micursor = database.cursor(buffered=True)
        
    
        
    
        micursor.execute("""
                    CREATE TABLE IF NOT EXISTS users( 
                    id int(25) AUTO_INCREMENT not null,
                    Nombre VARCHAR(100) not null,
                    Apellidos VARCHAR(255) default 'NULL',
                    Email VARCHAR(255) NOT NULL unique,
                    Password VARCHAR(255) NOT NULL,
                    Fecha date NOT NULL,
                    constraint pk_mynote primary key(id)
                    )
                    
                    """)
        
        micursor.execute("""
                    CREATE TABLE IF NOT EXISTS notas( 
                    id int(25) AUTO_INCREMENT not null,
                    Usuario_id int(25) not null,
                    Titulo VARCHAR(255) NOT NULL,
                    Descripcion mediumtext default 'NULL',
                    Fecha date NOT NULL,
                    constraint pk_mynote primary key(id),
                    constraint fk_mynote foreign key(Usuario_id) references users(id)
                    )
                    
                    """)
        
        print("Conectado a la base de datos")
        

    except:
        print("No se pudo conectar a la base de datos")
        print("Presione enter para continuar, una vez que haya solucionado el problema")

    return [database, micursor]
    

