import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class MyEmail:
    def __init__(self, smtp: str, imap: str, login: str, password: str):
        self.smtp = smtp
        self.imap = imap
        self.login = login
        self.password = password

    def send_message(self, subject: str, recipients: list, message: str):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(self.smtp, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login, recipients, message, msg.as_string())

        ms.quit()

    def recieve_message(self, header):
        mail = imaplib.IMAP4_SSL(self.imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()

        return email_message


if __name__ == '__main__':
    email = MyEmail("smtp.gmail.com", "imap.gmail.com", 'login@gmail.com', 'qwerty')
    email.send_message('Subject', ['vasya@email.com', 'petya@email.com'], 'Message')
    email.recieve_message(None)
