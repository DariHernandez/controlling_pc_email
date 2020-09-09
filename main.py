#! python3
# Controlling pc with email

import logging, os
from readEmail import readEmails
from rwJsonFile import readJsonFile
from interfaz import runInterfaz

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable()

# Files and initial vars
currentDir = os.path.dirname(__file__)
credentailsPath = os.path.join(currentDir, 'credentials.json')


# Run interfaz
credentials = runInterfaz (credentailsPath)
if credentials: 
    # Acces to IMAP

    # Get credentials
    imap = credentials['imap']
    myEmail = credentials['myEmail']
    password = input ('Your password of %s: ' % myEmail)
    fromEmail = credentials['fromEmail']
    folder = credentials['folder']
    search = credentials['search']

    # Acess and return all menssage
    allEmails = readEmails (imap, myEmail, password, folder, search)
    print(allEmails) 
    





# Open unreaded emails

# Check the from emails and the content

    # If the email if to Controlling pc, run file with instructions

# Run each 15 minutes with cron