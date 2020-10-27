#! python3
# Read email and access to IMAP

import imapclient, pyzmail, sys

def readEmails (imap, myEmail, password, folder, search): 
    """ Get all emails from folder and search termns"""
    try: 
        imapObj = imapclient.IMAPClient(imap, ssl=True)
    except: 
        print ('Connection error. Check your IMAP. --help for more information.')
        sys.exit()
    
    try: 
        imapObj.login(myEmail, password)
    except: 
        print ('Login error. Check your email and password. --help for more information.')
        sys.exit()
    
    try:
        imapObj.select_folder(folder, readonly=True)
    except: 
        print ('Folder dosent exist. Check your credentials. --help for more information.')
        sys.exit()

    try: 
        UIDs = imapObj.search([search])
    except: 
        print ('Search termn error. Try SEEN or UNSEEN. Check your credentials. --help for more information.')
        sys.exit()

    dicReturn = {}

    for uid in UIDs: 
        rawMessage = imapObj.fetch([uid],  ['BODY[]', 'FLAGS'])
        message = pyzmail.PyzMessage.factory(rawMessage[uid][b'BODY[]'])
        fromEmail = message.get_address('from')
        subject = message.get_subject()
        text = ''
        if message.text_part: 
            text = message.text_part.get_payload().decode(message.text_part.charset)
            text = text[:-2]
        dicReturn[uid] = {'fromMail': fromEmail, 
                            'text': text, 
                            'subject': subject}
    
    return dicReturn

def deleteMails  (imap, myEmail, password, folder, UIDs): 
    """Delete specific mails"""
    imapObj = imapclient.IMAPClient(imap, ssl=True)
    imapObj.login(myEmail, password)
    imapObj.select_folder(folder, readonly=False)

    imapObj.delete_messages(UIDs)
    imapObj.expunge()

def filterMails (infoDic, fromEmail, secretWord):
    """ return only the emails with specific command word and from email"""
    dicReturn = {}
    for uid, mailInfo in infoDic.items():
        from_   = mailInfo['fromMail']
        text    = mailInfo['text']
        subject = mailInfo['subject']
        
        if from_[1] == fromEmail and secretWord in subject and len(text.split()) == 1: 
            dicReturn [uid] = {'fromMail': fromEmail, 
                                'text': text, 
                                'subject': subject}

    return dicReturn


