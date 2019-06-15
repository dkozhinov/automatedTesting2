__author__ = 'Dmitry Kozhinov'

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib
import os


def deletefile(filename):
    if os.path.isfile(filename):
        os.remove(filename)


def sendemail(filename):
    sendemail_host = "smtp.mail.ru"
    sendemail_subject = "Screenshot from automated testing by python"
    sendemail_to_address = "d.kozhinov@mail.ru"
    sendemail_from_address = "mytest19741106@mail.ru"
    sendemail_from_password = "Qwer123$"
    sendemail_text = "This email has been sent automatically. No answer required."

    # Создаем email сообщение
    msg = MIMEMultipart()
    msg['From'] = sendemail_from_address
    msg['To'] = sendemail_to_address
    msg['Subject'] = sendemail_subject

    # Добавляем текст в сообщение
    msg.attach(MIMEText(sendemail_text, 'plain'))

    # Добавляем файл скриншота в сообщение
    if os.path.isfile(filename):
        with open(filename, 'rb') as fp:
            img = MIMEImage(fp.read())
            fp.close()
            msg.attach(img)

    deletefile(filename)

    server = smtplib.SMTP_SSL(sendemail_host, 465)
    server.login(sendemail_from_address, sendemail_from_password)
    server.send_message(msg)
    server.quit()
