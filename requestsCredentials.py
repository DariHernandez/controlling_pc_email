#! python3
# Request specific credentials of the project

from rwJsonFile import writeJsonFile
from credentials import validateCredentail, returnCredentials, returnCredential, printCredentials

def requestsCredentials (credentailsPath): 
    """ Request all the credentials"""
    print ('Please capture your information\n')
    myEmail      = validateCredentail('Your email (example: example@mail.com): ', content='@')
    imap         = validateCredentail('IMAP server of your email. (examle: imap.gmail.com): ', content='imap')
    folder       = validateCredentail('Folder emails (examle: INBOX): ', lenght=3)
    search       = validateCredentail('Email search terms (examle: UNSEEN): ', lenght=3)
    fromEmail    = validateCredentail('The from email (example: fromEmail@mail.com): ', content='@')  
    word         = validateCredentail('Command words, sparated by white space (example: play study work): ', content='')  
    wordsList     = word.split()

    credentials = {'myEmail': myEmail.strip(), 
                    'imap': imap.strip(),
                    'folder': folder.strip().upper(),
                    'search': search.strip().upper(),
                    'fromEmail': fromEmail.strip(),
                    'wordsList': wordsList}

    print ('\nNew credentials saved.\n')
    writeJsonFile (credentailsPath, credentials)