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


def contains_uppercase(password):

    for char in password:
        if char.isupper():
            return True
    return False


def contains_symbols(password):

    for char in password:
        if char in string.punctuation:
            return True
    return False


if __name__ == '__main__':

    num_password = int(input("How many passwords do you want to generate?  "))
    length = int(input("What is the length of the passwords?  "))
    uppercase = input("Can contain uppercase? y/n   ")
    symbols = input("Can contain symbols? y/n  ")

    if uppercase.lower() == 'y':
        uppercase = True
    else:
        uppercase = False

    if symbols.lower() == 'y':
        symbols = True
    else:
        symbols = False
    print()
    for i in range(1, num_password+1):
        new_pass = generate_password(length, uppercase, symbols)
        new_pass_check = f"U: {contains_uppercase(new_pass)}, S: {contains_symbols(new_pass)}"
        print(f"{i} ->  {new_pass}   {new_pass_check}")
