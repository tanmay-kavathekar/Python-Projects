import smtplib
from smtplib import SMTP
import getpass



from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from_addr=input("Please enter your email id: ")
from_pass=getpass.getpass("Enter password: ")
to_addr=input("Please enter recipient's email id:  ")

msg= MIMEMultipart()
msg['From']=from_addr
msg['To']=to_addr
msg['Subject']=input("Enter subject of the email: ")

msg.preamble='Multipart message.\n'

body=input("Enter text to send:  ")
msg.attach(MIMEText(body))

filename=input("Enter path of the file with extension: ")
attachment=open(filename,"rb")

part=MIMEBase('application','octet-stream')
part.set_payload((attachment).read())

encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment',filename=filename)

msg.attach(part)

server= smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(from_addr,from_pass)
text=msg.as_string()
server.sendmail(from_addr,to_addr,text)
server.quit()
