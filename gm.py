import smtplib

r_email ='jothikarthi2015@gmail.com'
s_email='k.gokulappaduraikjgv@gmail,com'
password='9489228333'
message='hi mom whats the lunch iam now angrey the garlic was peeled'
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(s_email,password)
print("LOGIN SUCCESS")
server.sendmail(s_email,r_email,message)

