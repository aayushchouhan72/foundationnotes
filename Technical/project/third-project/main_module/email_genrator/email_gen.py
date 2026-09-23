import smtplib
from email.message import EmailMessage

# Local imports 
from main_module.llm_module.similar_search import getmodel

def sendanmail():
     reason =input("enter why you wont to write an email....")
     receivers =  input("Enter receiver email....") 
     llm=getmodel()
     res = llm.invoke