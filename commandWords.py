#! python3
# Get command words from mail information

def getCommandWords (wordsList, infoDic, fromEmail, secretWord):
    """ return command words from info emails"""
    commandWords = []
    for mailInfo in infoDic.values():
        from_   = mailInfo['fromMail']
        text    = mailInfo['text']
        subject = mailInfo['subject']
        
        if from_[1] == fromEmail and secretWord in subject and len(text.split()) == 1: 
            commandWords.append(text)

    return commandWords