import smtplib
from email.message import EmailMessage
from  rich.console import Console
from rich.markdown import Markdown

# Local imports 
from main_module.llm_module.similar_search import getmodel
from main_module.email_genrator.utility import genrate_email,edit_genrated_mail,sendmail
from main_module.output_fromated.output import fromated_output
def email():
     con=Console()
     reason =input("enter why you wont to write an email....")
     receivers =  input("Enter receiver email....") 
     email=""
     email=fromated_output(reason,"Genrate an email for this resone")
     while True:
          check= input("Enter yes if wont continue if wont any edit then enter what did you wont to edit ....")
          if check ==  'yes':
                    break       
          email=fromated_output(f"{email}this is email edit it according to given instrucation",check)
     if sendmail(email,receivers):
            print("✅✅Email sent successfully ..")
     else:
            print("email not sent succesfully ..")
     
          
          
          
                   
