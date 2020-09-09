#! python3
# Basic terminal interfaz

import sys
from rwJsonFile import readJsonFile
from requestsCredentials import returnCredentials, returnCredential, requestsCredentials, printCredentials

def runInterfaz (credentailsPath): 
    credentials = returnCredentials (credentailsPath)
    if credentials:
        if sys.argv [1:] == ['--help'] or sys.argv [1:] == ['help']:
            menssage = 'write "-c -list" to see all credentials '
            menssage += '\nwrite "-c -edit" to edit all credentials '
            menssage += '\nwrite none arguments to run the program and Controlling pc with email'
            print (menssage)
            sys.exit()
        elif sys.argv [1:] == ['c'] or sys.argv [1:] == ['-c']:
            menssage = 'write "-c -list" to see all credentials '
            menssage = '\nwrite "-c -edit" to edit all credentials '
            print (menssage)
            sys.exit()
        elif sys.argv [1:] == ['-c', '-list']:
            # Return list of credentials
            printCredentials(credentailsPath)
            sys.exit()
        elif sys.argv [1:] == ['-c', '-edit']:
            # Edit credentials file
            requestsCredentials(credentailsPath)
            credentials = returnCredentials (credentailsPath)
            sys.exit()
        else: 
            print ('Running program...')
            return credentials
    else:  
        print ('No registred credentials.')
        requestsCredentials (credentailsPath)
        sys.exit()
    