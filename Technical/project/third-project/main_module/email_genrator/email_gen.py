import smtplib
from email.message import EmailMessage
from  rich.console import Console
from rich.markdown import Markdown

# Local imports 
from main_module.llm_module.similar_search import getmodel
from main_module.email_genrator.utility import genrate_email,edit_genrated_mail,sendmail
def email():
     con=Console()
     reason =input("enter why you wont to write an email....")
     receivers =  input("Enter receiver email....") 
     email=""
     email=genrate_email(reason)
     con.print(Markdown(email))
     while True:
          check= input("Enter yes if wont continue if wont any edit then enter what did you wont to edit ....")
          if check ==  'yes':
                    break       
          email=edit_genrated_mail(email,check)
          con.print(Markdown(email))
     if sendmail(email,receivers):
            print("✅✅Email sent successfully ..")
     else:
            print("email not sent succesfully ..")
     
          
          
          
                   
