#! python3
# Run an get specific secuence of commands
import webbrowser, subprocess

import logging, os

currentDir = os.path.dirname(__file__)
logPath = os.path.join(currentDir, 'logs.txt')

logging.basicConfig(filename=logPath, level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


def commandsRun (word, commands):
    """ Run specific secuence of commands"""
    for name, commandsList in commands.items(): 
        if word.lower() == name.lower(): 
            for command in commandsList: 
                try: 
                    exec(command)
                    logging.info(command)
                except: 
                    print ('Error to execute command "%s"' % command)
                    logging.warning(command)

def getCommandWords (infoDic, fromEmail, secretWord):
    """ return command words from info emails"""
    commandWords = []
    for mailInfo in infoDic.values():
        from_   = mailInfo['fromMail']
        text    = mailInfo['text']
        subject = mailInfo['subject']
        
        if from_[1] == fromEmail and secretWord in subject and len(text.split()) == 1: 
            commandWords.append(text)

    return commandWords