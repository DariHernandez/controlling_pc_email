#! python3
# Run an get specific secuence of commands
import webbrowser, subprocess

def commandsRun (word, commands):
    """ Run specific secuence of commands"""
    for name, commandsList in commands.items(): 
        if word.lower() == name.lower(): 
            for command in commandsList: 
               exec(command)

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