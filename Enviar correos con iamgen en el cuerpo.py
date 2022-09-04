""" with open(filename="img.jpg", mode="rb") as archivo:
    print(archivo.read()) 
    
    file = open("Imagen.jpg", "rb")
attach_image = MIMEImage(file.read())
attach_image.add_header('Content-Disposition', 'attachment; filename = "Alarma"')
msg.attach(attach_image)
    
    """
    
    
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from smtplib import SMTP
import os,sys





# Codigo keylogger
def keylogger():
    # Codigo limpiar archivo

    # Codigo email

    def email():

        msg = MIMEMultipart("plain")
        msg["From"] = "pruebapersonal182@outlook.com"
        msg["To"] = "jroatoro362@gmail.com"
        msg["Subject"] = "Recuperacion de contraseña MYNOTE"

        msg.attach(MIMEText("fhbsdufuvbdsfhbguhsdfuvbu", 'plain'))

        

        #adjntar una iamgen
        """ image_file = open(r'./Proyecto practico/modelo/img.jpg','rb').read()
        pic = MIMEImage(image_file)
        pic.add_header('Content-Disposition','attachment',filename='mynote.jpg')
        msg.attach(pic) """
        
        
        htmlFile = """\
        <html>
            <head></head>
            <body>
            <br>
            <br>
                <img src="cid:image1">
                
            </body>
        </html>
        """
        htmlpart = MIMEText(htmlFile,'html','utf-8')
        msg.attach(htmlpart)

        #Muestra imágenes en el cuerpo
        imagenDirectory = './Proyecto practico/modelo/img/img.png'
        image = MIMEImage(open(imagenDirectory,'rb').read(),imagenDirectory.split('.')[-1])
        # Definir ID de imagen, citar en texto HTML
        image.add_header('Content-ID','<image1>')
        msg.attach(image)
    
    
    
        

        smtp = SMTP("smtp.office365.com", 587)
        smtp.starttls()
        smtp.login("pruebapersonal182@outlook.com", "1825Jorge")
        smtp.sendmail("pruebapersonal182@outlook.com",
                      "jroatoro362@gmail.com", msg.as_string())
        smtp.quit()
        print("Correo enviado, verifique su bandeja de entrada")

    email()




keylogger()
