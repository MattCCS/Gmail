import base64
import datetime
import email
import os
import smtplib


SMTP_SERVER = os.environ['SMTP_SERVER']
SMTP_PORT = int(os.environ['SMTP_PORT'])
SMTP_USERNAME = os.environ['SMTP_USERNAME']
SMTP_PASSWORD = os.environ['SMTP_PASSWORD']

EMAIL_FROM = SMTP_USERNAME

DATE_FORMAT = "%d/%m/%Y"
EMAIL_SPACE = ", "


def send_email(email_to,
               email_subject,
               email_body,
               email_from=EMAIL_FROM,
               reply_to=None,
               withDate=False):

    if not isinstance(email_to, list):
        email_to = [email_to]

    msg = email.MIMEMultipart.MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = EMAIL_SPACE.join(email_to)
    msg['Reply-To'] = reply_to if reply_to else email_from
    msg['Subject'] = email_subject + ((" " + datetime.date.today().strftime(DATE_FORMAT)) if withDate else "")

    msg.attach( email.MIMEText.MIMEText('\n' + email_body) )

    if SMTP_PORT == 587:
        mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    elif SMTP_PORT == 465:
        mail = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    else:
        raise RuntimeError("unknown SMTP_PORT")

    mail.ehlo() # !!!
    # mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(email_from, email_to, msg.as_string())
    mail.quit()
