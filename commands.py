#! python3
# Run an get specific secuence of commands
import webbrowser, subprocess
import logging, os, csv

currentDir = os.path.dirname(__file__)
logPath = os.path.join(currentDir, 'logs.txt')

logging.basicConfig(filename=logPath, level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


def getCommandWords (filterMails):
    """ return command words from info emails"""
    commandWords = []
    for mailInfo in filterMails.values():
        text    = mailInfo['text']
        commandWords.append(text)

    return commandWords


def getFiles (path): 
    """ Return a list of csv files in specific folder"""
    csvFiles = []
    files = os.listdir (path)
    for file in files: 
        if file.endswith('.csv'): 
            csvFiles.append (file)
    return csvFiles

def printFiles (path): 
    """ Print csv files (only the name)"""
    files = getFiles(path)
    print ('The commands are:')
    for file in files: 
        name = str(os.path.basename (file))[:-4]
        print (name)

def check_path (path, pathType): 
    check = False
    if pathType == "dir": 
        check = os.path.isdir(path)
    elif pathType == "file": 
        check = os.path.isfile(path)
    elif pathType == "exist": 
        check = os.path.exists(path)
    return check

def request_command_file (menssage, pathType): 
    while True: 
        command = input ('%s \n- ' % menssage)
        if check_path (command, pathType): 
            return command
        else: 
            print ('Incorrect path, try again')

def addCommand (path): 
    """ Add new command to files"""
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
            command = input ('Type the web page:')
        # Request program
        elif key == 2: 
            command = request_command_file ('Type the complite path of the program:', "file")
        # Request program and file
        elif key == 3:
            command = request_command_file('Type the complite path of the program that will open the file:', "file")
            file = request_command_file('Type the file path:', "exist")

        # Write the file
        pathCSV = os.path.join (path, fileName + '.csv')
        fileCSV = open (pathCSV, 'a')
        writerSCV = csv.writer (fileCSV)
        writerSCV.writerow ([key, command, file])

        # Chedck loop
        other = input ('Other instruction (y/n)')
        if other.lower()[0] != 'y': 
            break


def runCommands (path, words): 
    """ Run the instrucctions in the files"""
    files = getFiles(path)

    # Verify the command words
    for word in words: 
        for file in files:
            if os.path.basename(file)[:-4] == word: 
                fileCSV = open (os.path.join(path, file), 'r')
                readerCSV = csv.reader (fileCSV)
                data = list (readerCSV)

                # Ganarate command
                for row in data:
                    if int(row[0]) == 1: 
                        command = "webbrowser.open('%s')" % (row[1])
                    elif int(row[0]) == 2: 
                        command = "subprocess.Popen('%s')" % (row[1])
                    elif int(row[0]) == 3: 
                        command = "subprocess.Popen(['%s','%s'])" % (row[1], row[1])
                
                    # Excect command
                    try: 
                        exec(command)
                        logging.info(command)
                    except: 
                        print ('Error to execute command "%s"' % command)
                        logging.warning(command)