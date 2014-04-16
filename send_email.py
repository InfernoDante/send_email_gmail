import smtplib
from email.mime.text import MIMEText

def send_email(message,subject,toaddrs):

    fromaddr = 'ENTER YOUR EMAIL ADDRESS'
    username = 'ENTER YOUR USERNAME'
    password = 'ENTER YOUR PASSWORD'
    
    
    msg = MIMEText(message, 'html')
    
    msg['Subject']  = subject
    
    msg['From']=fromaddr
    
    msg['Reply-to'] = 'no-reply'
    
    msg['To'] = toaddrs
    
    server = smtplib.SMTP('smtp.gmail.com:587')
    
    server.starttls()
    
    server.login(username,password)
    
    server.sendmail(fromaddr, [toaddrs], msg.as_string())
    server.quit()
   


subject = raw_input("Enter your subject?\n")
message = raw_input("Enter your mesage?\n")
toaddrs = raw_input("Enter receiver email address?\n")
send_email(str(message),str(subject),str(toaddrs))