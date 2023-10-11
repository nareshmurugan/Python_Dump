import os
import smtplib

EMAIL_ADDRESS= os.environ.get('DB_USER')
EMAIL_PASSWORD = os.environ.get('DB_PASS')

with smtplib.SMTP('smtp.gmail.com',587)as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    subject='hi mom whats the lunch'
    body='iam now angrey the garlic was peeled'

    msg=f'Subject: {subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADDRESS,'jothikarthi2015@gmail.com',msg)
