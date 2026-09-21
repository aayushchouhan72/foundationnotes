import smtplib
from email.message import EmailMessage
from io import BytesIO
def get_email():
    while True:
         email =  input("Enter the email to send qr ...")
         if email.endswith("@gmail.com") or email.endswith("@yahoo.com"):
               return email          
def get_level():
    while True:
        level =  input("Enter the Level HARD|EASY|MEDIUM :- ").lower().strip()
        if level == "hard" or level == "easy" or level == "medium":
                    return level
        else:
            print("Enter the valid defficulty level")

def sendmail(receiver, image_data):

    sender = "ayushnono4@gmail.com"

    msg = EmailMessage()

    msg["Subject"] = "QR Code"
    msg["From"] = sender
    msg["To"] = receiver

    msg.set_content("Hello! I have attached the QR code.")

    image_bytes = BytesIO()
    image_data.save(image_bytes, format="PNG")


    image_data = image_bytes.getvalue()


    msg.add_attachment(
        image_data,
        maintype="image",
        subtype="png",
        filename="qr_code.png"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, "fpfi wemt ggax nnot")
        smtp.send_message(msg)

    print("✅ Email sent successfully!")