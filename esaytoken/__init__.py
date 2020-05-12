from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import json
import random, string

##
## METHOD 
## ASE 128 
## CBC

MODE = AES.MODE_CBC


key_size = (16, 24, 32)


# u can gene a key by ''.join(random.sample(string.ascii_letters+string.digits, 16)).encode('utf-8')
block_size = 16



# 补16
def add_to_16(str):
    if len(str.encode('utf-8')) % 16:
        add = 16 - (len(str.encode('utf-8')) % 16)
    else:
        add = 0
    str = str + ('\0' * add)
    return str.encode('utf-8')



def encrypt(str,AES_SECRET_KEY=None,IV=None):

    kwargsCheck(AES_SECRET_KEY = AES_SECRET_KEY  ,IV = IV)


    mode = MODE
    str = add_to_16(str)
    cryptos = AES.new(AES_SECRET_KEY, mode, IV)
    cipher_str = cryptos.encrypt(str)

    return b2a_hex(cipher_str)


# strip取空格
def decrypt(str,AES_SECRET_KEY=None,IV=None):

    kwargsCheck(AES_SECRET_KEY = AES_SECRET_KEY  ,IV = IV)



    mode = MODE
    cryptos = AES.new(AES_SECRET_KEY, mode, IV)
    plain_str = cryptos.decrypt(a2b_hex(str))
    return bytes.decode(plain_str).rstrip('\0')


def get(eStr,key,AES_SECRET_KEY=None,IV=None):

    kwargsCheck(AES_SECRET_KEY = AES_SECRET_KEY  ,IV = IV)


    d = decrypt(eStr,AES_SECRET_KEY=AES_SECRET_KEY,IV=IV)
    dic = json.loads(d)
    value = dic.get(key)
    return value



def authcheck(eStr,key,AES_SECRET_KEY=None,IV=None):

    kwargsCheck(AES_SECRET_KEY = AES_SECRET_KEY,IV = IV)


    d = decrypt(eStr,AES_SECRET_KEY=AES_SECRET_KEY,IV=IV)
    dic = json.loads(d)
    value = dic.get(key)
    if int(value) == 1 :
        return True
    else :
        return False


def kwargsCheck(**kwargs):
    if kwargs['AES_SECRET_KEY']:
        pass
    else: 
        raise ValueError("AES key can not be None")
    if len(kwargs['AES_SECRET_KEY']) not in key_size:
        raise ValueError("Incorrect AES k   ey length (%d bytes)" % len(kwargs['AES_SECRET_KEY']))
    if len(kwargs['IV']) != block_size:
        raise ValueError("Incorrect AES key length (%d bytes)" % len(kwargs['IV']))
