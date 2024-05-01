from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

from main import SUPPORTED_LENS

IV_LEN = 16

class Crypter:
    def __init__(self, key_len, key_filename='key.pem'):
        if key_len not in SUPPORTED_LENS:
            raise Exception("Unsupported key length")
        self.key_len = key_len // 8
        self.key_filename = key_filename
    
    def gen_crypt_key(self):
        key = get_random_bytes(self.key_len)
        with open(self.key_filename, "wb") as out:
            out.write(key)
            
    def read_crypt_key(self) -> bytes:
        with open(self.key_filename, "rb") as inp:
            key = inp.read()
        return key
    
    def encrypt(self, string: str) -> str:
        byte_string = string.encode()
        cipher = AES.new(self.read_crypt_key(), AES.MODE_CBC)
        ciphered_string = cipher.iv + cipher.encrypt(pad(byte_string, AES.block_size))
        return ciphered_string.hex()

    def decrypt(self, crypted_string: str) -> str:
        bytes_data = bytes.fromhex(crypted_string)
        iv = bytes_data[:IV_LEN]
        data = bytes_data[IV_LEN:]
        cipher = AES.new(self.read_crypt_key(), AES.MODE_CBC, iv=iv)
        decrypted_data = unpad(cipher.decrypt(data), AES.block_size)
        decode_data = decrypted_data.decode()
        
        return decode_data
    