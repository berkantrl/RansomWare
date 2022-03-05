from Crypto.PublicKey import RSA 
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP



key = RSA.generate(2048)

private_key = key.export_key()
with open ('private.pem', 'wb') as file:

    file.write(private_key)

public_key = key.publickey().export_key()
with open('public.pem', 'wb') as file:
    file.write(public_key)


