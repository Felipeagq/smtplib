import smtplib



def CrearEmail(
    user: str,
    password: str,
    recep: str,
    subject: str,
    body: str
):
    email = f"\From: {user}\nSubject: {subject}\n\n{body}" 
    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login(user=user, password=password)
        server.sendmail(user,recep,email)
        server.close()
        print("Enviado correctamente")
    except:
        print("Fallido") 



CrearEmail(
    user="darkwpooh@gmail.com",
    password="Winniepooh22",
    recep="darkwpooh@gmail.com",
    subject="Hola",
    body="testing"
)