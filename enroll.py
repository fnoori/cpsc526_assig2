#
#   Developed by:       Farzam Noori
#   UCID:               10121495
#   Course:             CPSC 526 - Network Security
#   Tutorial:           03
#   Assignemnt:         2 (Programming Part)
#
#   This program takes 2 command line arguments:
#       argv[1]: username
#       argv[2]: password
#
#*******************************************************************

import sys
import enchant
import json
import re
import argon2
import random

REJECTED = "rejected"
ACCEPTED = "accepted"
CREDENTIALS = "credentials.json"

def main():
    username = sys.argv[1]
    password = sys.argv[2]

    if userAlreadyExists(username):
        rejected()

    if checkPassword(sys.argv[2]):
        accepted(username, password)


def checkPassword(password):
    # check if password is just numbers
    if password.isdigit():
        rejected()

    # check if password is a single English word
    # extract all letters from password to check if they're words
    extractedWord = "".join(re.findall("[a-zA-Z]+", password))
    if isWord(password) or isWord(extractedWord):
        rejected()

    return True


# check if username already exists
def userAlreadyExists(username):
    userExists = False

    with open(CREDENTIALS, "r") as file:
        try:
            fileContents = json.load(file)

            # find the username in the password file
            if fileContents[username]:
                userExists = True
            else:
                userExists = False
        except:
            userExists = False

    return userExists


# check if input is an English word
def isWord(input):
    wordChecker = enchant.Dict("en_US")

    if (wordChecker.check(input)):
        return True
    else:
        return False


# acceptance function
def accepted(username, password):
    userData = {}
    fileContents = {}

    # read file, even if it's empty
    with open(CREDENTIALS, "r") as outfile:

        # check if file is empty
        try:
            fileContents = json.load(outfile)
        except:
            '''do nothing'''
    
    # generate unique salt for user
    salt = generateSalt()
    hashedPassword = str(argon2.argon2_hash(password=password, salt=salt))
    userData[username] = {
        "password": hashedPassword,
        "salt": salt
    }

    fileContents.update(userData)

    with open("credentials.json", "w") as outfile:
        json.dump(fileContents, outfile)

    print(ACCEPTED)


# random salt from random library
def generateSalt():
    salt = ""
    for i in range(0, 15):
        salt += str(random.randint(0, 9))

    return salt


# generic reject function
def rejected():
    print(REJECTED)
    sys.exit(-1)    


# program start point
main()
