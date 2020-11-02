# controlling_pc_email
## Description
This is a terminal project.
With this program you will **control your pc via email(open files, open programs and open web pages)**

After configurate your email information and instrucctions, the program will be: 

**1. Access to you email.**
**2. Read the new email from the inbox.**
**3. Validate information: from mail, secret word and instrucction.**
**4. Run a group of previously configured instrucctions.**
**5. Delete the email from the inbox.**

# Install modules

```bash
$ pip3 install Send2Trash
$ pip3 install IMAPClient
$ pip3 install pyzmail
```

# How to use
## Credentials
The **first time** that you run the program, it **will request your information**: 

* **myEmail**: your email address
* **pass**: password of your email
* **fromEmail**: sender of emails with the intrucctions to the pc. the *fromEmail could be the same of myEmail*
* **imap**: imap server. This if in function of the email that you use. You can find the right server by searching in google.
* **folder**: folder to search emails Use INBOX for default configuration.
* **search**: search criteria Use UNSEEN for default configuration.
* **secretWord**: word in the subject of email. A short password for added security.

## Instrucctions

After the credentials, the program will **request the instructions**.

With the terminal menu, you can create as **many keywords as you want**, and each keyword is **linked to a group of instructions**, which can be: 
* **open a web page** 
* **open a program**
* **open a file with a specific program**

The web pages needs the complite url example: "https://github.com/"; and the programs and files need the complite path, example: "/home/user/Projects/file.txt" or "c:\users\myUser\desktop\file.txt"

## Terminal

You can run the program by terminal (main.py) **to see and edit your information or instrucctions**. 

```bash
$ python3 main.py --help

# write '-l --cred' to see all credentials. 
# write '-l --keys' to see all instrucction keys. 
# write '-l --keys KEYNAME' to see all instrucctions from specific key. 

# write '-e --cred' to edit all credentials. 
# write '-e --keys --add' to add new keys and instrucctions. 

# write '-d --keys KEYNAME' to delete a specific key."
        
```

## Emails

The emails to run the instructions, need to have the next sintaxis

* **sender**: the sender of the email is the same that **fromEmail** from credentials. 
* **subject**: the subject is your secret word.
* **body**: the body is the key/name of the instrucctions. 

## Automate
To automate this project and constantly read your emails looking for emails to execute instructions, I recommend using **Task Scheduler on Windows**, **launchd on OS X**, or the **cron scheduler on Linux** for lunch the programs at specific time (for example, **each 10 minutes**).

# Use example

## Credentials

Credentials request example

``` bash

$ myEmail (your email address):
# myemail@gmail.com

$ pass (password of your email)
# "my secret password"

$ fromEmail (sender of emails with the intrucctions to the pc)
# myotheremail@gmail.com

$ imap (imap server (example: imap.gmail.com))
# imap.gmail.com

$ folder (folder to search emails (example: INBOX))
# INBOX

$ search (search criteria (example: UNSEEN))
# UNSEEN

$ secretWord (word in the subject of email)
# SECRETKEY
``` 

## Instrucctions

Example of instrucctions: **ganerate two** keywords, the first will **open a web page** and the second keyword **open a program and a file**

``` bash
$ Type the key for the instrucction
# github

$ 1. Open web page 
$ 2. Run program 
$ 3. Open file
# 1

$ Type the web page: 
# https://github.com/

$ Other instruction (y/n) 
# y

$ Type the key for the instrucction
# project

$ 1. Open web page 
$ 2. Run program 
$ 3. Open file
# 2

$ Type the complite path of the program:  
# /usr/bin/code

$ Other instruction (y/n) 
# y

$ Type the key for the instrucction
# project

$ 1. Open web page 
$ 2. Run program 
$ 3. Open file
# 3

$ Type the complite path of the program:  
# /usr/bin/calibre

$ Type the file path: 
# /usr/documents/project/my_code.py

$ Other instruction (y/n) 
# n
``` 

## Emails example

Email to open a web page

![Email to open a web page](https://github.com/DariHernandez/controlling_pc_email/blob/master/secreenshots/email_github.jpg)

Email to open a program and a file

![Email to open a program and a file](https://github.com/DariHernandez/controlling_pc_email/blob/master/secreenshots/email_project.jpg)
