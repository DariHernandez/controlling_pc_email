#! python3
# Specific interfaz for the program

import sys
from interfaz import runInterfaz
from requestsCredentialsAndCommands import returnCredentials, returnCredential, requestsCredentials, printCredentials, requestsCommands

def runInterfazCrdentialsCommands (credentialsPath, commandsPath): 
    """ Run interfaz to request credetials and commands"""
    #commands = runInterfaz (commandsPath, 'commands', printCredentials, requestsCommands, returnCredentials, 'comm')
    credentials = runInterfaz (credentialsPath, 'credentials', printCredentials, requestsCredentials, returnCredentials, 'c')
    commands = runInterfaz (commandsPath, 'commands', printCredentials, requestsCommands, returnCredentials, 'com')
    
    if not credentials or not commands: 
        sys.exit()
    elif credentials == 'help' and commands == 'help': 
        print ('write none arguments to run the program and Controlling pc with email')
        sys.exit()
    elif credentials == 'error' and commands == 'error': 
        print ('Syntaxis error... write --help for more information')
        sys.exit()
    
    info = {'credentials': credentials,
            'commands': commands}    
    return info
