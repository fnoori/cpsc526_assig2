# Command line arguments:
#   username:
#       username can't be previously enrolled
#
#   password:
#       password is not simple:
#           "[word], [num], [wordnum], and [numword]" are forbidden
#
#
#   if username/passwrod confrom to the requirements:
#       print "accepted"
#       username/password stored in password file
#       exit code 0
#       
#   otherwise:
#       print "rejected"
#       exit code -1
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
#
'''
    jsonData = json.loads(open(CREDENTIALS).read())

    try:
        print(jsonData["usr1"])
    except KeyError:
        print("user doesn't exist")

    return
'''
#*******************************************************************

import sys
import enchant
import json
import re
import argon2

REJECTED = "rejected"
ACCEPTED = "accepted"
CREDENTIALS = "credentials.json"

def main():
    username = sys.argv[1]
    password = sys.argv[2]

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

def isWord(input):
    wordChecker = enchant.Dict("en_US")

    if (wordChecker.check(input)):
        return True
    else:
        return False


def accepted(username, password):
    userData = {}
    fileContents = {}
    isFileEmpty = False

    with open(CREDENTIALS, "r") as outfile:
        try:
            fileContents = json.load(outfile)
            isFileEmpty = True
        except:
            print("file empty")
            isFileEmpty = False
        

    hashedPassword = argon2.argon2_hash(password=password, salt="BLAH")
    userData[username] = {
        "password": password,
        "salt": "BLAH"
    }

    fileContents.update(userData)

    with open("credentials.json", "w") as outfile:
        json.dump(fileContents, outfile)

    print(ACCEPTED)


def rejected():
    print(REJECTED)
    sys.exit(-1)    


# program start point
main()
