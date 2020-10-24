#! python3
# Controlling pc with email

import os, pprint, logging
from readEmail import readEmails, deleteMails, filterMails
from commands import getCommandWords, addCommand, getFiles, runCommands
from interfaz import Interfaz

# Files and initial vars
currentDir = os.path.dirname(__file__)
pathCommands = os.path.join (currentDir, 'commands')
pathCredentails = os.path.join(currentDir, 'credentials.json')
pathConfig = os.path.join(currentDir, 'config.json')
commandsPath = os.path.join(currentDir, 'commands.json')
logPath = os.path.join(currentDir, 'logs.txt')

# Run interfaz
myInterfaz = Interfaz (pathCredentails, pathConfig)
commandsInterfaz = Interfaz (commandsPath, pathConfig)

# Get credentials
credentials = myInterfaz.getCredentials()
myEmail    = credentials['myEmail']
password   = credentials['pass']
fromEmail  = credentials['fromEmail']
imap       = credentials['imap']
folder     = credentials['folder']
search     = credentials['search']
secretWord = credentials['secretWord']

# Acess and return all menssage
allEmails = readEmails (imap, myEmail, password, folder, search)

# Get command words
filterMails = filterMails (allEmails, fromEmail, secretWord)
commandWords = getCommandWords (filterMails)

if commandWords: 
    # Check the command files and run instrucctions
    filesCSV = getFiles (pathCommands)
    if filesCSV:
        runCommands (pathCommands, commandWords)
    else: 
        addCommand (pathCommands)
    
    # Delete read menssage
    UIDs = []
    for keys in filterMails.keys(): 
        UIDs.append(keys)
    deleteMails  (imap, myEmail, password, folder, UIDs)
else:
    logging.info ('No new command emails.')
    print ('No new command emails. Check the information of the new emails.')


"""
    if commandWords: 
        # Run command files
        for word in commandWords: 
            commandsRun(word, credentialsCommands['commands'])
        

    
# Run each 15 minutes with cron
"""