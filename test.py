#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyelliptic import Cipher, ECC
from binascii import hexlify, unhexlify

print("TEST: AES-256-CTR")
ciphername = "aes-256-ctr"
iv = unhexlify(b"f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff")
key = unhexlify(b"603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4")
plaintext = unhexlify(b"6bc1bee22e409f96e93d7e117393172a")

ctx = Cipher(key, iv, 1, ciphername=ciphername)
enc = ctx.ciphering(plaintext)
print(hexlify(enc))

ctx = Cipher(key, iv, 0, ciphername=ciphername)
assert ctx.ciphering(enc) == plaintext


print("\nTEST: AES-256-CFB")
ciphername = "aes-256-cfb"
key = unhexlify(b"603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4")
iv = unhexlify(b"000102030405060708090A0B0C0D0E0F")
plaintext = unhexlify(b"6bc1bee22e409f96e93d7e117393172a")

ctx = Cipher(key, iv, 1, ciphername=ciphername)
enc = ctx.ciphering(plaintext)
print(hexlify(enc))

ctx = Cipher(key, iv, 0, ciphername=ciphername)
assert ctx.ciphering(enc) == plaintext


print("\nTEST: AES-256-CBC")
ciphername = "aes-256-cbc"
iv = unhexlify(b"000102030405060708090A0B0C0D0E0F")
key = unhexlify(b"603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4")
plaintext = unhexlify(b"6bc1bee22e409f96e93d7e117393172a")

ctx = Cipher(key, iv, 1, ciphername=ciphername)
enc = ctx.ciphering(plaintext)
print(hexlify(enc))

ctx = Cipher(key, iv, 0, ciphername=ciphername)
assert ctx.ciphering(enc) == plaintext


print("\nTEST: ECIES")
alice = ECC()
plaintext = b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ciphertext = ECC.encrypt(plaintext, alice.get_pubkey())
print(hexlify(ciphertext))
assert alice.decrypt(ciphertext) == plaintext


print("\nTEST: ECIES/RC4")
alice = ECC()
plaintext = b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ciphertext = ECC.encrypt(plaintext, alice.get_pubkey(), ciphername="rc4")
print(hexlify(ciphertext))
assert alice.decrypt(ciphertext, ciphername="rc4") == plaintext
