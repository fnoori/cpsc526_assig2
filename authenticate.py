#
#   Developed by:       Farzam Noori
#   UCID:               10121495
#   Course:             CPSC 526 - Network Security
#   Tutorial:           03
#   Assignemnt:         2 (Programming Part)
#
#   Authenticate Program
#
#   This program takes 2 command line arguments:
#       argv[1]: username
#       argv[2]: password
#
#*******************************************************************

import sys
import json
import argon2

ACCESS_GRANTED = "access granted\n"
ACCESS_DENIED = "access denied\n"
CREDENTIALS = "credentials.json"

def main():
    username = sys.argv[1]
    password = sys.argv[2]

    if loginUser(username, password):
        accessGranted()
    else:
        accessDenied()


def loginUser(username, password):
    loginResult = False
    jsonPassword = ""
    jsonSalt = ""

    with open(CREDENTIALS, "r") as file:
        try:
            fileContents = json.load(file)

            # see if username exists, if not, access denied
            if not(fileContents[username]):
                loginUser = False
            else:
                jsonPassword = fileContents[username]["password"]
                jsonSalt = fileContents[username]["salt"]

                # hash given password
                hashedPassword = str(argon2.argon2_hash(password=password, salt=jsonSalt))

                # check if stored (hashed) password is same as the hashed inputted password
                if jsonPassword == hashedPassword:
                    loginUser = True
                else:
                    loginUser = False
        except:
            # if file fails to read, access denied
            accessDenied()

    return loginUser


# generic access granted
def accessGranted():
    print(ACCESS_GRANTED)
    sys.exit(0)


# generic access denied
def accessDenied():
    print(ACCESS_DENIED)
    sys.exit(-1)



# runs only when it is not called via import
if __name__ == "__main__":
   main()