#! python3
import json, os, sys
from rwJson import readJsonFile, writeJsonFile
from commands import printCommands, deleteCommands, addCommand, printFiles

class Interfaz ():
    """Class to execute an interface from terminal, managing user credentials"""
    # Read and write json files

    def __init__ (self, pathCredentialsFile, pathConfigCredentialsFile):
        """ Run the inefaz"""
        """Run the complite interfaz"""

        # Initical vars
        self.credentailsPath = pathCredentialsFile
        self.configCredentialsPath = pathConfigCredentialsFile


        # Menssages
        helpMenssage = "\n write '-l --cred' to see all credentials. \
                        \n write '-l --keys' to see all instrucction keys. \
                        \n write '-l --keys KEYNAME' to see all instrucctions from speicif key. \
                        \n write '-e --cred' to edit all credentials. \
                        \n write '-e --keys --add' to add new keys and instrucctions. \
                        \n write '-d --keys KEYNAME' to delete a specific key."
        
        errorMenssage = "Incorrect input. Write --help for more information"

        # Run interfaz
        if len(sys.argv) == 2: 
            if sys.argv [1] == '--help':
                # Print help menssage
                print (helpMenssage)
            else: 
                print (errorMenssage)
            sys.exit()
        elif  len(sys.argv) > 2:
            if sys.argv [1] == '-l':
                # List json and csv files info
                if sys.argv [2] == '--keys':
                    # Return list of keys or instrucctions
                    if len(sys.argv) == 4: 
                        # print instrucctions from a file
                        printCommands (sys.argv [3])
                    else: 
                        # print list of keys
                        printFiles ()                    
                elif sys.argv [2] == '--cred':
                    # Return list of info
                    self.printCredentials()
                else: 
                    print (errorMenssage)
            elif sys.argv [1] == '-e':
                # Edit json files
                if sys.argv [2] == '--keys' and len(sys.argv) == 4:
                    if sys.argv[3] == '--add': 
                        # add keys
                        addCommand ()
                    else: 
                        print (errorMenssage)
                elif sys.argv [2] == '--cred':
                    # Requet credentials
                    self.requestCredentials()
                else: 
                    print (errorMenssage)
            elif sys.argv [1] == '-d' and sys.argv [2] == '--keys' and len(sys.argv) == 4:
                # Delete epecific key
                deleteCommands (sys.argv [3])
            else: 
                print (errorMenssage)
            sys.exit()

        # Read files. 
        configCredentials = readJsonFile (pathConfigCredentialsFile)
        credentials = readJsonFile (pathCredentialsFile)

        # if files are empty, requet it
        if not configCredentials: 
            self.requestConfigCredentials ()
        
        if not credentials: 
            self.requestCredentials ()

    def printCredentials (self): 
        """ Print a list of the credentials"""
        credentials = readJsonFile(self.credentailsPath)
        if credentials: 
            for name, credential in credentials.items(): 
                print (name, ': ', credential)
        else: 
            print ("No credentials yet")

    def printConfigCredentials (self): 
        """ Print a list of the config of credentials"""
        credentialConfigCounter = 0
        configCredentials = readJsonFile(self.configCredentialsPath)
        if configCredentials: 
            for configCredentail in configCredentials: 
                credentialConfigCounter += 1
                print (credentialConfigCounter)
                for name, value in configCredentail.items(): 
                    print (name, ': ', value)
        else: 
            print ("No config of credentials yet")

    def requestConfigCredentials (self): 
        """Set the info for request credentials"""
        # Request setting for credentials

        print ('\nPlease, capture configuration of credentials')

        credentialCounter = 1
        credentialsSettings = []
        while True: 
            # Request credentiual settings
            name = input ('Credential %s name: ' % credentialCounter)
            description = input ('Credential %s description: ' % credentialCounter)
            validation = input ('Credential %s validation: ' % credentialCounter)
            other = input ('Other credential? (y/n): ')
            
            # Add current credential to list
            credentialsSettings.append ({'name': name, 
                                        'description': description, 
                                        'validation': validation})

            if other.strip()[0] != 'y': 
                break

            credentialCounter += 1
            
        # Write credentials settings in the file
        writeJsonFile (self.configCredentialsPath, credentialsSettings)

    def requestCredentials (self): 
        """ Request the credentials with the credentials configuration file"""
        credentials = {}

        print ("\nPlase, capture your information")

        # Get configuration for each credential
        configCredentials = readJsonFile (self.configCredentialsPath)

        # Request to user each credential
        for configCredential in configCredentials: 
            while True:
                # Extract config info
                name = configCredential['name']
                description = configCredential['description']
                validation = configCredential['validation']
                # Request credential and add to the dictionary
                credential = input (name + ' (%s): ' % description)
                # Validate credential
                try: 
                    validation = int (validation)
                    if len(credential) >= validation: 
                        break
                    else: 
                        print ('Incorrect lenght. The credential needs at least %s characters' % int (validation))
                except: 
                    # Convert validation items to list
                    if validation: 
                        # Convert validation info to python data
                        if ',' in validation:
                            validation = json.loads (validation)
                        
                        if type (validation) != list:
                            validation = [validation] 

                        # Count correct validations
                        validationCounter = 0                
                        for validationItem in validation: 
                            if validationItem in credential: 
                                validationCounter += 1
                            else: 
                                print ('The credential needs to have "%s"' % validationItem)
                        
                        # Check number of validations
                        if validationCounter == len (validation): 
                            break
                    else: 
                        break

            credentials [configCredential['name']] = credential

        # Save credentials
        writeJsonFile (self.credentailsPath, credentials)

    def getCredentials (self): 
        credentials = readJsonFile (self.credentailsPath)
        return (credentials)
