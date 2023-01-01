import hashlib
import dict_crack_enhance_latest as dict

common = dict.common

passwd_hash = '5c916794deca0f7c3eeaee426b88f8bd'
passwd_found = None

try:
    with open(r'c:\temp\pass.txt', 'r+') as passwords:
        words = ','.join(str(word) for word in common)
        passwords.write(words)        
        word_split = words.split(',')
        print(word_split)
    
        for word in word_split:
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
except IOError as err:
    print(f'{err}')
except FileNotFoundError as err:
    print(f'{err}')
except Exception as err:
    print(f'{err}')


