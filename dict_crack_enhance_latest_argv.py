""" Script: dict_crack.py
Description: Cracks password hash using a dictionary of common passwords.
Author: Petra L
Modified: Sept 2019
"""
import hashlib
import sys

TRACE = True

# list of common passwords
common = [
    "123",
    "1234",
    "12345",
    "123456",
    "1234567",
    "12345678",
    "password",
    "qwerty",
    "abc",
    "abcd",
    "abc123",
    "111111",
    "monkey",
    "arsenal",
    "letmein",
    "trustno1",
    "dragon",
    "baseball",
    "superman",
    "iloveyou",
    "starwars",
    "montypython",
    "cheese",
    "123123",
    "football",
    "batman",
]


def check_pass(passwd_hash: str) -> bool:
    """ method to check a valid password hash"""
    hex_words = "0123456789abcdef"
    flag = True
    if len(passwd_hash) == 32 and isinstance(passwd_hash, str):
        for password in passwd_hash:
            if password not in hex_words:
                flag = False
                break
    return flag


def dict_attack(passwd_hash):
    """Dictionary attack, checks password hash
    against a list of common passwords using a loop"""
    print(f"[*] Cracking hash: {passwd_hash}")
    passwd_found = None

    for word in common:
        check_word = hashlib.md5(word.encode("utf-8"))
        check_upper = hashlib.md5(word.upper().encode("utf-8"))
        check_capital = hashlib.md5(word.title().encode("utf-8"))

        if check_word.hexdigest() == passwd_hash:
            passwd_found = word
        elif check_upper.hexdigest() == passwd_hash:
            passwd_found = word.upper()
        elif check_capital.hexdigest() == passwd_hash:
            passwd_found = word.title()
            break

    if passwd_found:
        print(f"[+] Password recovered: {passwd_found}")
    else:
        print(f'[-] Password not recovered {"."}')


def print_args(arg_list):
    """print out the arguments passed in as a list"""
    for arg in arg_list:
        print(f'{sys.argv.index(arg)}: {arg}')    
    print(f'[print_args] Args: {arg_list}')


def main():
    """ Set hash signature and match with the password """
#     print("[dict_crack] Tests")
#     passwd_hash = "4297f44b13955235245b2497399d7a93"
#     dict_attack(passwd_hash)
#     passwd_hash = "4297f44b13955235245b2497399d7a92"
#     dict_attack(passwd_hash)
#     passwd_hash = "5f4dcc3b5aa765d61d8327deb882cf99"
#     dict_attack(passwd_hash)
#     passwd_hash = "5badcaf789d3d1d09794d8f021f40f0e"
#     dict_attack(passwd_hash)
#     passwd_hash = "0d107d09f5bbe40cade3de5c71e9e9b7"
#     dict_attack(passwd_hash)
#     passwd_hash = " 5c916794deca0f7c3eeaee426b88f8bd"
#     # a space contains at start
#     dict_attack(passwd_hash)
#     passwd_hash = "5c916794deca0f7c3eeaee426b88f8bd"
#     dict_attack(passwd_hash)
#     passwd_hash = "a67778b3dcc82bfaace0f8bc0061f20e"
#     dict_attack(passwd_hash)
    passwd_hash = '12345678912345678912345678z92314'
    passhash = check_pass(passwd_hash)
    
    if passhash:
        dict_attack(passwd_hash)
    else:
        print(f'{passwd_hash} is not a valid hash')
    for arg in sys.argv:
        if len(sys.argv) > 1:
            passwd_hash = sys.argv[sys.argv.index(arg)]
            pas_hash = check_pass(passwd_hash)
            if pas_hash:
                dict_attack(passwd_hash)
            else:
                print(f"{passwd_hash} is not the correct password hash.")
            dict_attack(passwd_hash)
        else:
            print('Usage: args.py argument1 [argument2] [argument3]')
            sys.exit(1)        


if __name__ == '__main__':
    if TRACE:
        print('[T] Module called as script, calling main()')
    main()
else:
    if TRACE:
        print('[T] Module imported as library, not calling main')

