from Crypto.Cipher import AES
from Crypto import Random

iv = Random.new().read(AES.block_size)

def aes_cfb_encrypt(img, key=123): 
  
    #Expects to get an image that is to be encrypted

    cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
    enc_data = cfb_cipher.encrypt(img)
    
    return enc_data 

def aes_cfb_decrypt(img, key=123): 
  
    #Expects to get an image that was encrypted earlier
    
    cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
    plain_data = cfb_decipher.decrypt(img)
    
    return plain_data