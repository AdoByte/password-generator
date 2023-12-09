import string
import secrets


def generate_password(length, uppercase: bool, symbol: bool):

    combination = string.ascii_lowercase + string.digits

    if uppercase:
        combination += string.ascii_uppercase

    if symbol:
        combination += string.punctuation

    new_password = ''

    for i in range(length):         # length of password to be generated
        new_password += combination[secrets.randbelow(len(combination))]        # len(combination) is the upper limit
        # for randbelow
    return new_password
