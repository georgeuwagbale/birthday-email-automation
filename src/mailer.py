import smtplib
from email.message import EmailMessage
from email.utils import make_msgid



class MailSender:
    def __init__(self, smtp_server: str, smtp_port: int, email_password: str):
        self.smtp_server: str = smtp_server
        self.smtp_port: int = smtp_port
        self.password: str = email_password
        self.msg = EmailMessage()

    def set_email_subject(self, email_subject: str):
        self.msg["Subject"] = email_subject

    def get_email_subject(self):
        return self.msg["Subject"]

    def set_email_sender(self, sender_email: str):
        self.msg["From"] = sender_email

    def get_email_sender(self):
        return self.msg["From"]

    def set_email_receiver(self, email_receiver: str):
        self.msg["To"] = email_receiver

    def get_email_receiver(self):
        return self.msg["To"]

    def set_email_content(self, email_content: str):
        self.msg.set_content(email_content)

    def add_html_with_image(self, image_path: str):
        asparagus_cid = make_msgid()
        self.msg.add_alternative(f"""\
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            
        </head>
        <body>
            <p>Internal use only</p>
            <div class="">
                <img src="cid:{asparagus_cid[1:-1]}" alt="Image"
                    style=" display: block;
                            margin-left: auto;
                            margin-right: auto;"
                            width="500"
                            height="700">
            </div>
        </body>
        </html>
        """, 
        subtype="html")
        # msgAlternative.attach(msgText)

        with open(image_path, 'rb') as img:
            self.msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg',
                                                  cid=asparagus_cid)

    def send_email(self):
        if self.get_email_receiver() and self.get_email_sender(): 
            try:
                self.server = smtplib.SMTP(self.smtp_server, self.smtp_port)
                # check connection
                self.server.starttls()
                self.server.login(self.get_email_sender(), self.password)
                # Send email here
                self.server.send_message(self.msg)# Email sends here
                self.server.quit()
            except Exception as e:
                print(e)

        elif self.get_email_receiver() == None and self.get_email_sender() == None:
            print("Sender's email and Receiver's email not set")
    def __str__(self):
        return self.msg

