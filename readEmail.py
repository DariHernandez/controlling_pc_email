#! python3
# Read email and access to IMAP

import imapclient, pyzmail, pprint

def readEmails (imap, myEmail, password, folder, search): 
    """ Get all emails from folder and search termns"""
    imapObj = imapclient.IMAPClient(imap, ssl=True)
    imapObj.login(myEmail, password)
    imapObj.select_folder(folder, readonly=True)
    UIDs = imapObj.search([search])

    dicReturn = {}

    for uid in UIDs: 
        rawMessage = imapObj.fetch([uid],  ['BODY[]', 'FLAGS'])
        message = pyzmail.PyzMessage.factory(rawMessage[uid][b'BODY[]'])
        fromEmail = message.get_address('from')
        text = ''
        if message.text_part: 
            text = message.text_part.get_payload().decode(message.text_part.charset)
        dicReturn[uid] = {'fromMail': fromEmail, 'text': text}
    
    return dicReturn

