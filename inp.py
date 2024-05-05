import click
import os
import crpt as mycrpt

def get_decrypted(string, crypter: mycrpt.Crypter):
    try:
        decrypted_string = crypter.decrypt(string)
    except:
        return ValueError("\033[31mОшибка при расшифровке!\033[0m")
    return decrypted_string


@click.group()
def cli():
    pass

@cli.command()
@click.option('--encrypt', default='')
@click.argument('key_path', type=str)
@click.argument('key_len', type=int)
def encrypt(encrypt, key_path, key_len):
    try:
        crypter = mycrpt.Crypter(key_len, key_path)
        crypter.gen_crypt_key()
    except:
        print("\n\033[31mПроизошла ошибка\033[0m! Проверьте длину ключа и/или путь к ключу шифрования")
        return
    login = input("\nInput login for encrypting: ")
    password = input("Input password for encrypting: ")
    print(f'\n\033[32mEncrypted login\033[0m: {crypter.encrypt(login)}')
    print(f'\033[32mEncrypted password\033[0m: {crypter.encrypt(password)}')
    print(f'\033[32mPath to the generated encryption key\033[0m: {os.path.abspath(crypter.key_filename)}\n')

@cli.command()
@click.option('--decrypt', default='')
@click.argument('key_path', type=str)
@click.argument('key_len', type=int)
def decrypt(decrypt, key_path, key_len):
    try:
        crypter = mycrpt.Crypter(key_len, key_path)   
    except:
        print("\n\033[31mПроизошла ошибка\033[0m! Проверьте длину ключа и/или путь к ключу шифрования")
        return
    
    raw_data = {"\n\033[32mDecrypted login\033[0m:": input("\nInput login for decrypting: "), 
                "\033[32mDecrypted password\033[0m:": input("Input password for decrypting: ") }
    decrypted = [get_decrypted(data, crypter) for data in list(raw_data.values())]
    for i in range(len(decrypted)):
        if type(decrypted) == ValueError:
            print(decrypted)
            return
        print(list(raw_data.keys())[i], decrypted[i])