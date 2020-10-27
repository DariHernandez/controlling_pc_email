#! python3
# Run an get specific secuence of commands
import webbrowser, subprocess, send2trash
import logging, os, csv

currentDir = os.path.dirname(__file__)
logPath = os.path.join(currentDir, 'logs.txt')

logging.basicConfig(filename=logPath, level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')


def getCommandWords (filterMails):
    """ return command words from info emails"""
    commandWords = []
    for mailInfo in filterMails.values():
        text    = mailInfo['text']
        commandWords.append(text)

    return commandWords

def getFiles (): 
    """ Return a list of csv files in specific folder"""
    currentDir = os.path.dirname (__file__)
    path = os.path.join (currentDir, 'commands')
    csvFiles = []
    files = os.listdir (path)
    for file in files: 
        if file.endswith('.csv'): 
            csvFiles.append (file)
    return csvFiles

def printFiles (): 
    """ Print csv files (only the name)"""
    files = getFiles()
    print ('The commands are:')
    for file in files: 
        name = str(os.path.basename (file))[:-4]
        print (name)

def request_command_file (menssage, pathType): 
    """ Request input user and validate"""
    while True: 
        command = input ('%s \n- ' % menssage)
        check = False

        # Validate path (input user)
        if pathType == "dir": 
            check = os.path.isdir(command)
        elif pathType == "file": 
            check = os.path.isfile(command)
        elif pathType == "exist": 
            check = os.path.exists(command)
        
        if check: 
            return command
        else: 
            print ('Incorrect path, try again')

def addCommand (): 
    """ Add new command to files"""
    currentDir = os.path.dirname (__file__)
    path = os.path.join (currentDir, 'commands')
    print ('Indicates what to do when an instruction email is received')
    while True:
        # File and key name
        fileName = input('\nType the key for the instrucction: ')

        while True:
            key = input ("Select what to do: \n1. Open web page \n2. Run program \n3. Open file\n- ")
            # Validate input
            try: 
                key = int(key)
                if key > 0 and key <= 3:
                    break
            except: 
                print ('\nOption error. Please, select only a number. Try again.\n')

        # request instruccion
        command = ""
        file = ""
        # Request web page
        if key == 1: 
            command = input ('Type the web page: ')
        # Request program
        elif key == 2: 
            command = request_command_file ('Type the complite path of the program: ', "file")
        # Request program and file
        elif key == 3:
            command = request_command_file('Type the complite path of the program that will open the file: ', "file")
            file = request_command_file('Type the file path: ', "exist")

        # Write the file
        pathCSV = os.path.join (path, fileName + '.csv')
        fileCSV = open (pathCSV, 'a')
        writerSCV = csv.writer (fileCSV)
        writerSCV.writerow ([key, command, file])

        # Chedck loop
        other = input ('Other instruction (y/n) ')
        if other.lower()[0] != 'y': 
            break

def runCommands (words): 
    """ Run the instrucctions in the files"""
    currentDir = os.path.dirname (__file__)
    path = os.path.join (currentDir, 'commands')
    files = getFiles()

    # Verify the command words
    for word in words: 
        for file in files:
            if os.path.basename(file)[:-4] == word: 
                fileCSV = open (os.path.join(path, file), 'r')
                readerCSV = csv.reader (fileCSV)
                data = list (readerCSV)

                print ('Running %s commands' % word)
                logging.info(word)

                # Ganarate command
                for row in data:
                    if int(row[0]) == 1: 
                        command = "webbrowser.open('%s')" % (row[1])
                    elif int(row[0]) == 2: 
                        command = "subprocess.Popen('%s')" % (row[1])
                    elif int(row[0]) == 3: 
                        command = "subprocess.Popen(['%s','%s'])" % (row[1], row[2])
                
                    # Excect command
                    try: 
                        exec(command)
                        logging.info(command)
                    except: 
                        print ('Error to execute command "%s"' % command)
                        logging.warning(command)

def deleteCommands (file): 
    """ Delete a specific CSV filw with instrucctions"""
    currentPath = os.path.dirname (__file__)
    pathFile = os.path.join (currentPath, 'commands', file  + '.csv')

    if os.path.exists (pathFile):
        delete = input('Do you want to delete this key with all instrucctions? (y/n) ')

        if delete.lower()[0] == 'y':
            send2trash.send2trash (pathFile)
            print ('%s deleted' % file)
    else: 
        print ('Key error. Try again. Use --help for more information.')

def printCommands (file): 
    """ Print each instrucction from a file """
    currentPath = os.path.dirname (__file__)
    pathFile = os.path.join (currentPath, 'commands', file + '.csv')
    print (pathFile)

    if os.path.exists (pathFile):
        # Open file
        fileCSV = open (os.path.join(pathFile), 'r')
        readerCSV = csv.reader (fileCSV)
        data = list (readerCSV)
        data.sort()

        # Print instrucctions
        print ('Instrucctions of "%s":' % file)
        for row in data: 
            if int(row[0]) == 1: 
                print ('web page: "%s"' % row[1])
            elif int(row[0]) == 2: 
                print ('program: "%s"' % row[1])
            elif int(row[0]) == 3: 
                print ('file: "%s", with program: "%s"' % (row[2], row[1]))

    else: 
        print ('Key error. Try again. Use --help for more information.')


