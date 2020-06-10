import requests
import re
import time
import smtplib
from getpass import getpass

class Gmail(object):
    def __init__(self, sender_email, receiver_email, password):
        self.sender_email = 'ilyvs105@gmail.com'
        self.receiver_email = 'ilyas.rysbekov@nu.edu.kz'
        # self.sender_email = None
        # self.receiver_email = None
        self.password = getpass()
        self.server = 'smtp.gmail.com'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)        
        session.starttls()
        session.login(self.sender_email, self.password)
        self.session = session

    def send_message(self, subject, body):

        headers = [
            "From: " + self.sender_email,
            "Subject: " + subject,
            "To: " + self.receiver_email,
            "MIME-Version: 1.0",
           "Content-Type: text/html"]

        headers = "\r\n".join(headers)
        self.session.sendmail(self.sender_email, self.receiver_email, headers + "\r\n\r\n" + body)

url = 'https://www.instagram.com/p/B7tvbqkputO/'
pattern1 = r'At least.*posted this pic'
pattern2 = r'Page.*bull; Instagra.*'

# url = 'https://www.instagram.com/p/BxSlOCxHDzl/'
# pattern1 = r'Through years'
# pattern2 = r'Page.*bull; Instagra.*'

sender_email = 'ilyvs105@gmail.com'
receiver_email = 'ilyas.rysbekov@nu.edu.kz'
password = getpass()

while True:
    delay = time.sleep(86400)
    res = requests.get(url, delay)
    if re.findall(pattern1, res.text):
        pass
    elif re.findall(pattern2, res.text):
# print('Single')
        gm = Gmail(sender_email, receiver_email , password)
        gm.send_message('Hi there', 'Single, brazzzzaaaaa :D This message is sent from Python')
        break

