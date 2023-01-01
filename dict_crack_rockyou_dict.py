"""dictionary_crack_rockyou.py to hash password by rockyou.txt"""
import hashlib

TRACE = True


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
    try:
        passwd_dict = {}
        # use 'latin-1' or 'cp437' encoding for rockyou.txt
        with open(r'rockyou.txt', encoding='cp437') as rock_you:
#             pass_list = [line.strip('\n') for line in rock_you]
            data = rock_you.read()
            data = data.strip('\n')
            pass_list = data.split('\n')
            for word in pass_list:
                hash_code = hashlib.md5(word.encode('utf-8')).hexdigest()
                passwd_dict[hash_code] = word

        # export hash and password to rockpass.txt in local dir
#         with open(r'c:\temp\rockpass.txt', 'w') as rockpass:
#             for key, val in passwd_dict.items():
#                 rockpass.write(key + " -> " + val + "\n")
                
        if passwd_hash in passwd_dict:
            found_pass = passwd_dict[passwd_hash]
            print(f"Password is {found_pass}")
        else:
            print("Password not found.")

    except IOError as err:
        print(f'{err}')
    except FileNotFoundError as err:
        print(f'{err}')
    except Exception as err:
        print(f'{err}')

def main():
    flag = False
    password_list = []
    while not flag:
        passwd = str(input('Enter Password Hash: '))
        password_list.append(passwd)
        confirm = str(input('Want to add another hash (Y/N) '))
        if confirm.lower() == 'n':
            flag = True
    for passwd_hash in password_list:        
        pas_hash = check_pass(passwd_hash)
        if pas_hash:
            dict_attack(passwd_hash)
        else:
            print(f"{passwd_hash} is not the correct password hash.")


if __name__ == '__main__':
    if TRACE:
        print('[T] Module called as script, calling main()')
    main()
else:
    if TRACE:
        print('[T] Module imported as library, not calling main')
    

