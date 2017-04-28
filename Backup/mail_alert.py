#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sbhar
#
# Created:     14/12/2016
# Copyright:   (c) sbhar 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import smtplib,getpass
from email.mime.multipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders

def sendMail(toMailId, name,latitude, longitude, cityName):
    mailTo=toMailId

    sender="sherlockholmesmc10@gmail.com"
    s=smtplib.SMTP("smtp.gmail.com",587)
    s.ehlo()
    s.starttls()
    pwd=#Some random password
    s.login(sender,pwd)


    msg=MIMEMultipart()
    msg["From"]=sender
    msg["To"] = mailTo
    msg['Subject']="Is your phone safe?"
    bodyText=""
    if cityName!='unknown':
    	bodyText='''Hi '''+name+''',

         I detected some suspicious activity in your phone. In case it is lost, it can be found at Latitude '''+str(latitude)+''', Longitude '''+str(longitude)+''', in the city of '''+cityName+'''. Good luck.

Regards,
Sherlock'''
    else:
	bodyText='''Hi '''+name+''',

         I detected some suspicious activity in your phone. Unfortunately, I couldn't track the location of your device. Please contact the authorities in case it is lost.

Regards,
Sherlock'''

    body=MIMEText(bodyText)
    msg.attach(body)
    s.sendmail(msg["From"],msg["To"],msg.as_string())
    s.close()
    #s.quit()

def main():
    sendMail('joeljmj26@gmail.com','joel', '33.4216338', '-111.9209028', 'Tempe')

if __name__ == '__main__':
    main()
