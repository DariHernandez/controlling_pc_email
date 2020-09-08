#! python3
# Request specific credentials of the project

from rwJsonFile import writeJsonFile
from credentials import validateCredentail, returnCredentials, returnCredential, printCredentials

def requestsCredentials (credentailsPath): 
    """ Request all the credentials"""
    print ('Please capture your information\n')
    myEmail   = validateCredentail('Your email (example: example@mail.com): ', content='@')
    smtp      = validateCredentail('SMPT server of your email. (examle: smtp.gmail.com): ', content='smtp')
    portSmtp  = validateCredentail('SMPT PORT server of your email. (examle: 587): ', lenght=2)
    fromEmail = validateCredentail('The from email (example: fromEmail@mail.com): ', content='@') 

    credentials = {'myEmail': myEmail, 
                    'smtp': smtp,
                    'portSmtp': portSmtp,
                    'fromEmail': fromEmail}

    print ('\nNew credentials saved.\n')
    writeJsonFile (credentailsPath, credentials)