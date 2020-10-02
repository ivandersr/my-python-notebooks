from string import Template
from dados_email import email_smtp, senha_smtp

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

with open('template.html', 'r') as html:
    template = Template(html.read())
    msg_body = template.safe_substitute(nome='Ivander', data='25/07/2024')

msg = MIMEMultipart()
msg['from'] = 'Ivander do Futuro'
msg['to'] = email_smtp
msg['subject'] = 'Continue, você finalmente está no caminho certo.'

corpo = MIMEText(msg_body, 'html')
msg.attach(corpo)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email_smtp, senha_smtp)
    smtp.send_message(msg)
