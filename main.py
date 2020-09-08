#! python3
# Controlling pc with email

import logging, os
from readEmail import readEmails
from rwJsonFile import readJsonFile
from interfaz import runInterfaz

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


# Files and initial vars
currentDir = os.path.dirname(__file__)
credentailsPath = os.path.join(currentDir, 'credentials.json')


# Run interfaz
crdentials = runInterfaz (credentailsPath)

    # Acces to IMAP




# Open unreaded emails

# Check the from emails and the content

    # If the email if to Controlling pc, run file with instructions

# Run each 15 minutes with cron