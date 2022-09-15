    
from mailjet_rest import Client
import modelo.users as users





class EnviarCorreo:
    try:
        def __init__(self,correoCliente="NULL@NULL.COM"):
            self.correoCliente = correoCliente
            self.contrasena = users.User("","",self.correoCliente).ConsultarPass()                 
            __api_key = '5b31c4ecaf1a928e06c296724708a8e3'
            __api_secret = '7aaef943931c72a0bf57b4c16081b3c3'
            self.mailjet = Client(auth=(__api_key, __api_secret), version='v3.1')
            
        def enviarCorreo(self):
            if self.contrasena == False:
                input("Presione enter para continuar")
            else:
            
                msg = {
                    'Messages': [
                        {
                        "From": {
                            "Email": "jlroa82@misena.edu.co",
                            "Name": "Jorge"
                        },
                        "To": [
                            {
                            "Email": self.correoCliente,
                            }
                        ],
                        "Subject": "Recuperacion de contraseña MYNOTE.",
                        "TextPart": "My first Mailjet email",
                        "HTMLPart": """<p>Hemos detectado que presenta inconvenientes para iniciar sesión en su cuenta MYNOTE.
                        A continuación encontrará la contraseña de acceso a su cuenta MYNOTE.</p><br />
                        CONTRASEÑA: {0} <br /><br /><br />Gracias por utilizar nuestros servicios.Cualquier duda o consulta no dude en contactarnos<br /><br />
                        <img src="https://play-lh.googleusercontent.com/1AaKzUP7GlKbKpil3TdkiCL01YxnowsMhN0unFoDKs92fBiUPGcL_nY1PhAoLBccx32D" width="200" height="200">
                        """.format(self.contrasena),
                        "CustomID": "AppGettingStartedTest"
                        }
                        ]
                    }
                                
                self.mailjet.send.create(data=msg)          
                print("\n==================================================================")
                print("Correo enviado,por favor verifique su bandeja de entrada o de spam")
                print("==================================================================")

    except:
            print("Critical error, sistema no disponible")




