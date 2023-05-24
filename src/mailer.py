import smtplib
from email.message import EmailMessage
from email.utils import make_msgid

class MailSender:
    def __init__(self, smtp_server: str, smtp_port: int, email_password: str) -> None:
        self._server = None
        self._smtp_server: str = smtp_server
        self._smtp_port: int = smtp_port
        self._password: str = email_password
        self._msg = EmailMessage()

    def set_email_subject(self, email_subject: str):
        self._msg["Subject"] = email_subject

    def get_email_subject(self):
        return self._msg["Subject"]

    def set_email_sender(self, sender_email: str):
        self._msg["From"] = sender_email

    def get_email_sender(self):
        return self._msg["From"]

    def set_email_receiver(self, email_receiver: str):
        self._msg["To"] = email_receiver

    def get_email_receiver(self):
        return self._msg["To"]

    def set_email_content(self, email_content: str):
        self._msg.set_content(email_content)

    def add_html_with_image(self, image_path: str):
        asparagus_cid = make_msgid()
        self._msg.add_alternative(f"""\
        <!DOCTYPE html>
        <html lang="en" 
            style="
                    height: 100%;
                    margin: 0;
            ">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            
        </head>
        <body style="height: 100%; margin: 0;">
            <p>Internal use only</p>
            <div>
                <img src="cid:{asparagus_cid[1:-1]}" alt="Image"
                    style=" display: block;
                            width: 100%;
                            z-index: 0;">
            </div>
            
        </body>
        </html>
        """,
                                  subtype="html")
        # msgAlternative.attach(msgText)

        with open(image_path, 'rb') as img:
            self._msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg',
                                                   cid=asparagus_cid)

    def send_email(self):
        if self.get_email_receiver() and self.get_email_sender() and self.get_email_subject():
            try:
                self._server = smtplib.SMTP(self._smtp_server, self._smtp_port)
                # check connection
                self._server.starttls()
                self._server.login(self.get_email_sender(), self._password)
                # Send email here
                self._server.send_message(self._msg)
                self._server.quit()
            except Exception as e:
                print(e)

        if self.get_email_receiver() is None:
            print("Receiver's email not set")

        if self.get_email_sender() is None:
            print("Sender's email not set")

        if self.get_email_subject() is None:
            print("Email subject not set")

    def __str__(self):
        return self._msg

