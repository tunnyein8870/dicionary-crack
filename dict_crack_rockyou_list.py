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
        passwd_found = None
        # use 'latin-1' or 'cp437' encoding for rockyou.txt
        with open(r'rockyou.txt', encoding='cp437') as rock_you:
            data = rock_you.read()
            data = data.strip("r\n")
            pass_list = data.split("\n")
#          pass_list = [line.strip("\n") for line in rock_you]

            for word in pass_list:
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
            print(f'There are {len(pass_list)} passwords in rockyou.txt')
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
    
# 4297f44b13955235245b2497399d7a93