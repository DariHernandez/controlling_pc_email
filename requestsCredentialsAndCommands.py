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
    

    credentials = {'myEmail': myEmail.strip(), 
                    'imap': imap.strip(),
                    'folder': folder.strip().upper(),
                    'search': search.strip().upper(),
                    'fromEmail': fromEmail.strip()}

    print ('\nNew credentials saved.\n')
    writeJsonFile (credentailsPath, credentials)

def requestsCommands (commandsPath): 
    """ Request all the commands """
    word         = validateCredentail('Command words, sparated by white space (example: play study work): ', content='')  
    keyWords     = word.split()

    dicCommands = {}

    print ('Please capture the commands to execute \n')
    for keyWord in keyWords: 
        commands = []
        print ('Commands to run with the keyword *%s*: (write "q" to end)' % keyWord)
        commandNum = 0
        while True: 
            commandNum +=1
            command = validateCredentail(menssage='command %s: ' % commandNum, content='')
            if command == "q": 
                break
            else: 
                commands.append(command)
        dicCommands [keyWord] = commands
    print ('\nNew commands saved.\n')
    writeJsonFile (commandsPath, dicCommands)