#! python3
# Read email and access to IMAP

import imapclient, pyzmail, pprint

def readEmails (): 
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imapObj.login('cidentymx@gmail.com', 'duscordia de ceguera temporal 87')
    imapObj.select_folder('INBOX', readonly=True)
    UIDs = imapObj.search(['UNSEEN'])

    dicReturn = {}

    for uid in UIDs: 
        rawMessage = imapObj.fetch([uid],  ['BODY[]', 'FLAGS'])
        message = pyzmail.PyzMessage.factory(rawMessage[uid][b'BODY[]'])
        fromMail = message.get_address('from')
        text = message.text_part.get_payload().decode(message.text_part.charset)
        dicReturn[uid] = {'fromMail': fromMail, 'text': text}
    
    return dicReturn