import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuração
host = 'mail.pix.com.br'
port = 587
user = 'naoresponda-qwcontrol@pix.com.br'
password = 'Pix@3000'

# Criando objeto
print('Criando objeto servidor...')
server = smtplib.SMTP(host, port)

# Login com servidor
print('Login...')
server.ehlo()
server.starttls()
server.login(user, password)

# Criando mensagem
print('Criando mensagem...')
email_msg = MIMEMultipart()
email_msg['From'] = user
email_msg['To'] = 'charles.bezerra@qwsoftware.com.br'
email_msg['Subject'] = 'Ele passa a mão!'
text = "Hi guys!"
html = """
<html>
        <head>
            <style type='text/css'>
              * {
                  margin: 0;
                  padding: 0;
                  outline: 0;
                  box-sizing: border-box;
                }
              .header {
                display: flex;
                width: 100%;
                background-color: rgb(205, 203, 203);
                align-items: center;
                justify-content: space-between;
              }
              .header img {
                width: 70px;
                margin-left: 20px;
                }
              .header h1 {
                margin-right: 20px;
                margin-left: 30%
              }
              .content {
                padding: 10px;
              }  
              .content p {
                font-size: 16px;
              }
            </style>       
        </head>        
            <div class='header'>
              <img src='https://qwcontrol.pix.com.br/static/images/favicon-152.png' alt='Logo' />
              <h1>Bem-vindo ao QWControl</h1>
            </div>
            <div class='content'>
              <p>
                As experiências acumuladas demonstram que a constante divulgação das informações auxilia a preparação e a composição das condições inegavelmente apropriadas.
              </p>
            </div>
        </body>
    </html>
 """

print('Adicionando texto...')
email_msg.attach(MIMEText(html, 'html'))

# Enviando mensagem
print('Enviando mensagem...')
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
print('Mensagem enviada!')
server.quit()
print('Conexão encerrada!')
