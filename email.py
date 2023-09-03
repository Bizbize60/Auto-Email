# -*- coding: utf-8 -*-
"""
Created on Mon May 22 19:35:09 2023

@author: BBS
"""
import webbrowser
import smtplib, ssl
import time
from datetime import datetime
from PyQt5.QtWidgets import *
import sys
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.properties()
    def properties(self):
        self.resize(800,800)
        self


port = 465  # For SSL
smtp_server = "smtp.yandex.com.tr"
sender_email = "BiGBoss1Shot@yandex.com"  
receiver_email = "fmesdur@thk.edu.tr"  
password = "gzzkbkggtogynbrf"
message = """\
Subject: Hi 

This message was sent you by Tunahan's alarm clock , he cannot wake and he has an important meeting please get him up
/attemp 2."""


a=int(input("Hour?"))
b=int(input("Minute?"))
while True:
    date=datetime.now()
    hour=int(date.hour)
    minute=int(date.minute)
    if a==hour and b==minute:
        webbrowser.open("https://www.youtube.com/watch?v=Sr7ZUlsTwKc")
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            break
        
    else:
       time.sleep(60)         

