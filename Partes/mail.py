from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


class Mail:
    def __init__ (self, msg, email='casonenhumsejainformado_definaumPadrão'):
        self.msg = msg 
        self.email = email
    
    def sendMail(self):
        # servidor:
        host = 'smtp-mail.outlook.com'
        port = 587
        usuario = self.email
        senha = ''
        with open('./.pwBD.txt', 'r') as f:
            senha = f.readlines()[1]
        servidor = smtplib.SMTP(host, port)

        # login
        servidor.ehlo()
        servidor.starttls() # criptografia
        servidor.login(usuario, senha)
        email = MIMEMultipart()
        email['From'] = 'insiraseuemail'
        email['To'] = 'insiraoemaildestino'
        email['Subject'] = 'Login'
        email.attach(MIMEText(self.msg, 'plain'))

        # enviando:
        servidor.sendmail(email['From'], email['To'], email.as_string())
        servidor.quit()
