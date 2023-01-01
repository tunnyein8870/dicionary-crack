""" Script: dict_crack.py
Description: Cracks password hash using a dictionary of common passwords.
Author: Petra L
Modified: Sept 2019
"""
import hashlib

# list of common passwords
common = ['123', '1234', '12345', '123456', '1234567', '12345678',
          'password', 'qwerty', 'abc', 'abcd', 'abc123', '111111',
          'monkey', 'arsenal', 'letmein', 'trustno1', 'dragon',
          'baseball', 'superman', 'iloveyou', 'starwars',
          'montypython', 'cheese', '123123', 'football', 'batman']


def dict_attack(passwd_hash):
    """Dictionary attack, checks password hash
    against a list of common passwords using a loop"""
    print(f"[*] Cracking hash: {passwd_hash}")
    passwd_found = None
    
    if isinstance(passwd_hash, str) and len(passwd_hash) == 32:
        for word in common:
            check_word = hashlib.md5(word.encode("utf-8"))
            check_upper = hashlib.md5(word.upper().encode("utf-8"))
            check_capital = hashlib.md5(word.title().encode("utf-8"))
            
            if check_word.hexdigest() == passwd_hash:
                passwd_found = word
                break
            elif check_upper.hexdigest() == passwd_hash:
                passwd_found = word.upper()
                break
            elif check_capital.hexdigest() == passwd_hash:
                passwd_found = word.title()
                break
            
        if passwd_found:
            print(f"[+] Password recovered: {passwd_found}")
        else:
            print(f'[-] Password not recovered {"."}')
    else:
        print(f'[#] Password hash must be string and has 32 chars.')

def main():
    """ Set hash signature and match with the password """
    print("[dict_crack] Tests")
    passwd_hash = "4297f44b13955235245b2497399d7a93"
    dict_attack(passwd_hash)
    passwd_hash = "4297f44b13955235245b2497399d7a92"
    dict_attack(passwd_hash)
    passwd_hash = "5f4dcc3b5aa765d61d8327deb882cf99"
    dict_attack(passwd_hash)
    passwd_hash = '5badcaf789d3d1d09794d8f021f40f0e'
    dict_attack(passwd_hash)
    passwd_hash = '0d107d09f5bbe40cade3de5c71e9e9b7'
    dict_attack(passwd_hash)
    passwd_hash = ' 5c916794deca0f7c3eeaee426b88f8bd'   # a space contains at start 
    dict_attack(passwd_hash)
    passwd_hash = '5c916794deca0f7c3eeaee426b88f8bd'
    dict_attack(passwd_hash)
    passwd_hash = 'a67778b3dcc82bfaace0f8bc0061f20e'
    dict_attack(passwd_hash)
    passwd_hash = 12345678912345678912345678912345
    dict_attack(passwd_hash)

if __name__ == "__main__":
    main()

