from excel_reader import ExcelReader
from mailer import MailSender
from write_on_image import Writer
from dotenv import load_dotenv
from os import getenv
import datetime as dt
from scheduler import Scheduler


def main():
    load_dotenv("../email.env")


    # Excel file varibales
    try:
        excel_sheet_path = getenv("EXCEL_SHEET_PATH")
        excel_active_sheet = getenv("EXCEL_ACTIVE_SHEET")
        column_no = getenv("COLUMN_NUMBER")


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
        doc: ExcelReader = ExcelReader(excel_sheet_path, int(column_no))
        doc.set_active_sheet(excel_active_sheet)
        month = dt.date.today().month
        day = dt.date.today().day
        birthday_celebrants = doc.get_celebrants_from_file(month, day)

        image = Writer("../img/birth1.jpg")
        image.write_on_image(birthday_celebrants)

        mail = MailSender(smtp_server,smtp_port, email_pass)
        mail.set_email_subject(email_subject)
        mail.set_email_sender(email_sender)
        mail.set_email_receiver(email_receiver)
        mail.set_email_content(email_content)
        mail.add_html_with_image(email_image_path)
        mail.send_email()
        print("Email sent successfully.", f"{dt.datetime.now().day} day, {dt.datetime.now().hour} hour, {dt.datetime.now().minute}, ")
    except Exception as e:
        print(e)

print("Starting")

schedule = Scheduler()
# schedule.daily(dt.time(hour=11), main)
schedule.cyclic(dt.timedelta(minutes=1), main)
print("started")
while True:
    schedule.exec_jobs()