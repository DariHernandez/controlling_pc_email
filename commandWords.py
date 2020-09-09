#! python3
# Get command words from mail information

def getCommandWords (wordsList, infoDic, fromEmail, secretWord):
    """ return command words from info emails"""
    commandWords = []
    for mailInfo in infoDic.values():
        from_ = mailInfo['fromMail']
        text = mailInfo['text']
        
        if from_[1] == fromEmail and secretWord in text and len(text.split()) == 2: 
            textItems = text.split()
            textItems.remove(secretWord)
            commandWords.append(textItems[0])

    return commandWords