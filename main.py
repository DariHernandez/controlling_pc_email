#! python3
# Controlling pc with email

import logging, os, pprint
from readEmail import readEmails
from rwJsonFile import readJsonFile
from interfaz import runInterfaz
from commandWords import getCommandWords
from commands import command

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
    imap       = credentials['imap']
    myEmail    = credentials['myEmail']
    password   = input ('Your password of %s: ' % myEmail)
    fromEmail  = credentials['fromEmail']
    folder     = credentials['folder']
    search     = credentials['search']
    wordsList  = credentials['wordsList']
    secredWord = input ('Your secret word in emails: ')

    # Acess and return all menssage
    allEmails = readEmails (imap, myEmail, password, folder, search)

    # Get command words
    commandWords = getCommandWords (wordsList, allEmails, fromEmail, secredWord)

    # Run command files
    for word in commandWords: 
        if word.strip().lower() in wordsList: 
            command(word)
    
    # Delete read menssage
    

# Run each 15 minutes with cron