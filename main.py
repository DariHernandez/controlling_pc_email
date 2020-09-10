#! python3
# Controlling pc with email

import logging, os, pprint
from readEmail import readEmails, deleteMails
from rwJsonFile import readJsonFile
from pcControlInterfaz import runInterfazCrdentialsCommands
from commands import getCommandWords, commandsRun

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable()

# Files and initial vars
currentDir = os.path.dirname(__file__)
credentailsPath = os.path.join(currentDir, 'credentials.json')
commandsPath = os.path.join(currentDir, 'commands.json')

# Run interfaz credentials
credentialsCommands = runInterfazCrdentialsCommands (credentailsPath, commandsPath)
if credentialsCommands: 
    # Run  interfaz commands

    # Get credentials
    imap       = credentialsCommands['credentials']['imap']
    myEmail    = credentialsCommands['credentials']['myEmail']
    password   = input ('Your password of %s: ' % myEmail)
    fromEmail  = credentialsCommands['credentials']['fromEmail']
    folder     = credentialsCommands['credentials']['folder']
    search     = credentialsCommands['credentials']['search']
    secredWord = input ('Your secret word in emails: ')

    # Acess and return all menssage
    allEmails = readEmails (imap, myEmail, password, folder, search)

    # Get command words
    commandWords = getCommandWords (allEmails, fromEmail, secredWord)

    if commandWords: 
        # Run command files
        for word in commandWords: 
            commandsRun(word, credentialsCommands['commands'])
        
        # Delete read menssage
        UIDs = []
        for keys in allEmails.keys(): 
            UIDs.append(keys)
        deleteMails  (imap, myEmail, password, folder, UIDs)
    else:
        print ('No new command mails')
    
# Run each 15 minutes with cron