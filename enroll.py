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

def main():
    username = sys.argv[1]
    password = sys.argv[2]

    checkPassword(sys.argv[2])

def checkPassword(password):
    wordChecker = enchant.Dict("en_US")

    if (wordChecker.check(password)):
        print("That's a word !")
    else:
        print("That's not a word !")

main()
