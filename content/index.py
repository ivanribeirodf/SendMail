# -*- coding: utf-8 -*-
import argparse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("##############################################################################")
print("############################       SEND MAIL    ##############################")
print("##############################################################################")

# Configuração
parser = argparse.ArgumentParser(description="QWControl Send mail")
parser.add_argument('MAILHOST', help='Host do servidor de email.')
parser.add_argument('MAILPORT', help='Port do servidor de email.')
parser.add_argument('MAILUSER', help='Usuário de email.')
parser.add_argument('MAILPASS', help='Senha do usuário.')
parser.add_argument('MAILTO', help='Email destino.')
parser.add_argument('MAILSUB', help='Assunto.')
parser.add_argument('MAILMSG', help='Texto:')


args = parser.parse_args()
MAILHOST = None
MAILPORT = None
MAILUSER = None
MAILPASS = None
MAILTO = None
MAILSUB = None
MAILMSG = None

if args.MAILHOST:
    MAILHOST = args.MAILHOST
if args.MAILPORT:
    MAILPORT = args.MAILPORT
if args.MAILUSER:
    MAILUSER = args.MAILUSER
if args.MAILPASS:
    MAILPASS = args.MAILPASS
if args.MAILTO:
    MAILTO = args.MAILTO
if args.MAILSUB:
    MAILSUB = args.MAILSUB
if args.MAILMSG:
    MAILMSG = args.MAILMSG

# Criando objeto
print('Criando objeto servidor...')
server = smtplib.SMTP(MAILHOST, MAILPORT)

# Login com servidor
print('Login...')
server.ehlo()
server.starttls()
server.login(MAILUSER, MAILPASS)

# Criando mensagem
print('Criando mensagem...')
email_msg = MIMEMultipart()
email_msg['From'] = MAILUSER
email_msg['To'] = '{MAILTO}'
email_msg['Subject'] = '{MAILSUB}'
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
                {MAILMSG}
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
