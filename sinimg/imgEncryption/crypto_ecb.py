from Crypto.Cipher import AES
from Crypto import Random

iv = Random.new().read(AES.block_size)

def aes_ecb_encrypt(img, key='asdjk@15r32r1234asdsaeqwe314SEFT'): 
  
    #Expects to get an image that is to be encrypted

    ecb_cipher = AES.new(key, AES.MODE_ECB, iv)
    enc_data = ecb_cipher.encrypt(img)
    
    return enc_data 

def aes_ecb_decrypt(img, key='asdjk@15r32r1234asdsaeqwe314SEFT'): 
  
    #Expects to get an image that was encrypted earlier
    
    ecb_decipher = AES.new(key, AES.MODE_ECB, iv)
    plain_data = ecb_decipher.decrypt(img)
    
    return plain_data