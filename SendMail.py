import smtplib, ssl



def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "sendermail"
    password = "sender_mail_password"
    receiver_email = "receiver_mail"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        
        server.starttls(context=context)
        
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        print(e)
    finally:
        server.quit()