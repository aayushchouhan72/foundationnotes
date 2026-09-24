import smtplib
from email.message import EmailMessage

# Local imports
from main_module.llm_module.similar_search import getmodel

# Genrate an forameted email ...
def proper_formated_email(email):
    llm=getmodel()
    res= llm.invoke(f"Make the proper mail like from given text and make subject and email comtent this is email {email} in proper text file not in md")
    return res.content
#  Genrate full email for resone ...
def genrate_email(reason):
    llm=getmodel()
    res = llm.invoke(f"Genrate an email for this resone {reason} this should be in proper fromat and with proper greating's only retuen email content and give responese in md file")
    return res.content
#  Edit an existing email ...
def edit_genrated_mail(mail,correction):
    llm=getmodel()
    res=llm.invoke(f"""
        Edit the given email {mail}according this changes {correction} and return only in email content proper md file ..
""")   
    return res.content   
#Send an email 
def sendmail(email,receiver):
    sender = "ayushnono4@gmail.com"
    msg = EmailMessage()

    msg["Subject"] = "Your email for leave"
    msg["From"] = sender
    msg["To"] = receiver
    email=proper_formated_email(email)
    msg.set_content(f"""Hello! I have attached this is your email from leave
       {email}
    """)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, "fpfi wemt ggax nnot")
        smtp.send_message(msg)
    return True
         