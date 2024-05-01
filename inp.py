import click
import os
import crpt as mycrpt

@click.group()
def cli():
    pass

@cli.command()
@click.option('--encrypt', default='')
@click.argument('key_path', type=str)
@click.argument('key_len', type=int)
@click.argument('login', type=str)
@click.argument('password', type=str)
def encrypt(encrypt, key_path, key_len, login, password):
    crypter = mycrpt.Crypter(key_len, key_path)
    crypter.gen_crypt_key()
    print(f'\n\033[32mEncrypted login\033[0m: {crypter.encrypt(login)}')
    print(f'\033[32mEncrypted password\033[0m: {crypter.encrypt(password)}')
    print(f'\033[32mPath to the generated encryption key\033[0m: {os.path.abspath(crypter.key_filename)}\n')

@cli.command()
@click.option('--decrypt', default='')
@click.argument('key_path', type=str)
@click.argument('key_len', type=int)
def decrypt(decrypt, key_path, key_len):
    login = input("\nInput login for decrypting: ")
    password = input("Input password for decrypting: ")
    crypter = mycrpt.Crypter(key_len, key_path)    
    print(f'\n\033[32mDecrypted login\033[0m: {crypter.decrypt(login)}')
    print(f'\033[32mDecrypted password\033[0m: {crypter.decrypt(password)}\n')