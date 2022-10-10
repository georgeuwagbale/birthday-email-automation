from excel_reader import ExcelReader
from mailer import MailSender
from write_on_image import Writer
from dotenv import load_dotenv
from os import getenv

load_dotenv("../email.env")


# Excel file varibales
excel_sheet_path = getenv("EXCEL_SHEET_PATH")
excel_active_sheet = getenv("EXCEL_ACTIVE_SHEET")
column_no = int(getenv("COLUMN_NUMBER"))


# Email client variables
smtp_server = getenv("SMTP_SERVER")
smtp_port = getenv("SMTP_PORT")
email_pass = getenv("EMAIL_PASS")
email_subject = getenv("EMAIL_SUBJECT")
email_content = getenv("EMAIL_CONTENT")
email_sender = getenv("EMAIL_SENDER")
email_receiver = getenv("EMAIL_RECEIVER")
email_image_path = getenv("EMAIL_IMAGE_PATH")

# Initializing an getting content from Excel document
doc: ExcelReader = ExcelReader(excel_sheet_path, column_no)
doc.set_active_sheet(excel_active_sheet)
birthday_celebrants = doc.get_celebrants_from_file()

image = Writer("../img/birth1.jpg")
image.write_on_image(birthday_celebrants)

mail = MailSender(smtp_server,smtp_port, email_pass)
mail.set_email_subject(email_subject)
mail.set_email_sender(email_sender)
mail.set_email_receiver(email_receiver)
mail.set_email_content(email_content)
mail.add_html_with_image(email_image_path)
mail.send_email()




