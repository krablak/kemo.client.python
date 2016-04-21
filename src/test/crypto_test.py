__author__ = 'jesus'
import sys
import os
sys.path.append(os.path.join("..","mods"))
from cryptogej import Cryptor
import binascii

import hashlib

if __name__ == "__main__":

    key_ascii = "tohle je super tajny kluuucs"
    key = hashlib.sha256(key_ascii).hexdigest()
    print key

    to_encrypt = "hola hola hola hola geji"

    iv, encrypted = Cryptor.encrypt(to_encrypt, key)
    print iv.encode('hex')
    print (iv+encrypted).encode('hex')

    cyphertext = binascii.b2a_base64(encrypted).rstrip()

    print (iv+cyphertext)

    decrypted = Cryptor.decrypt(cyphertext, key, iv)

    print decrypted
    print len(iv), iv