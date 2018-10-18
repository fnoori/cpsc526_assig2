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
#*******************************************************************

import sys
import enchant

REJECTED = "rejected"

def main():
    username = sys.argv[1]
    password = sys.argv[2]

    checkPassword(sys.argv[2])

def checkPassword(password):

    # check if password is a single English word
    if (isWord(password)):
        print(REJECTED)
        sys.exit(-1)

    # check if password is just numbers
    

def isWord(input):
    wordChecker = enchant.Dict("en_US")

    if (wordChecker.check(input)):
        return True
    else:
        return False

main()
