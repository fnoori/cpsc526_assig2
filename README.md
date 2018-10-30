# CPSC 526      

|||
| ------------- |:-------------------:|
| **Developed by**  | Farzam Noori        |
| **UCID**          | 10121495            |
| **Tutorial**      | 03                  |
| **Assignemnt**    | 2 (Programming Part)|
| **Operating System**    | MacOS Mojave (10.14)|
| **Python**    | 3.7|


## Introduction
Enroll and authenticate users, using Argon2 as the hashing algorithm.

Testing using pytest.

**Please note that there are 2 users already populated in ```credentials.json```, this is for testing purposes only**

## Parts
* Enroll
  1. Navigate to program directory
  2. Run by typing in ```python3 enroll.py <username> <password>```
* Authenticate
  1. Navigate to program directory
  2. Run by typing in ```python3 authenticate.py <username> <password>```
      * **username must already exist**
* Unit Test
  1. Install py.test library
  2. Navigate to project directory
  3. Run by typing in ```pytest```
      * If you want a verbose output, type in ```pytest -v```
  * **Note**
    * **The description of the unit tests are specified in the unit test files as function comments**

## Library Used
* enchant
* argon2
* pytest

## Links to libraries used
Links to external libraries used

|||
| ------------- |:-------------------:|
| **Argon2**    | https://pypi.org/project/argon2/        |
| **pyenchant** | https://pypi.org/project/pyenchant/|
