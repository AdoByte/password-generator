import string
import secrets


def generate_password(length, uppercase: bool, symbols: bool):

    combination = string.ascii_lowercase + string.digits

    if uppercase:
        combination += string.ascii_uppercase

    if symbols:
        combination += string.punctuation

    new_password = ''

    for r in range(length):         # length of password to be generated
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
    pass_length = int(input("What is the length of the passwords?  "))
    allow_uppercase = input("Can contain uppercase? y/n   ")
    allow_symbols = input("Can contain symbols? y/n  ")

    if allow_uppercase.lower() == 'y':
        allow_uppercase = True
    else:
        allow_uppercase = False

    if allow_symbols.lower() == 'y':
        allow_symbols = True
    else:
        allow_symbols = False
    print()
    for i in range(1, num_password+1):
        new_pass = generate_password(pass_length, allow_uppercase, allow_symbols)
        new_pass_check = f"U: {contains_uppercase(new_pass)}, S: {contains_symbols(new_pass)}"
        print(f"{i} ->  {new_pass}   {new_pass_check}")
