import os
import random


class DH_Endpoint(object):



    def __init__(self,client_public_key=None,server_public_key=None, private_key=None):
        if client_public_key==None:
            self.client_public_key = None
            self.server_public_key = None
            self.private_key = None
            self.full_key = None
        else:
            self.client_public_key = client_public_key
            self.server_public_key = server_public_key
            self.private_key = private_key
            self.full_key = None

    def generate_partial_key(self):
        partial_key = self.client_public_key**self.private_key
        partial_key = partial_key%self.server_public_key
        return partial_key

    def generate_full_key(self, partial_key_client):
        full_key = partial_key_client**self.private_key
        full_key = full_key%self.server_public_key
        self.full_key = full_key
        return full_key


    def encrypt_message(self, msg):
        key = chr((self.full_key + 2) % 65536)
        keys = ''
        while len(keys) != len(msg):
            for i in key:
                if len(keys) != len(msg):
                    keys = keys + i
                else:
                    break
        nmsg = ''
        for i in range(len(keys)):
            i = (ord(msg[i]) - ord(keys[i])) % 65536
            nmsg = nmsg + chr(i)
        return nmsg

    def decrypt_message(self, encrypted_message):
        decrypted_message = ""
        key = chr((self.full_key + 2) % 65536)
        keys = ''
        while len(keys) != len(encrypted_message):
            for i in key:
                if len(keys) != len(encrypted_message):
                    keys = keys + i
                else:
                    break
        for i in range(len(keys)):
            i = (ord(encrypted_message[i]) + ord(keys[i])) % 65536
            decrypted_message = decrypted_message + chr(i)
        return decrypted_message


    def bunch_of_public_keys(self):
        with open('Open_keys.txt', 'r+') as file:
            if (os.path.exists('Open_keys.txt') and os.path.getsize('Open_keys.txt')) > 0:
                k = file.read()
                k = k.split(' ')
                self.private_key = int(k[0])
                self.client_public_key = int(k[1])
                self.server_public_key = random.randint(1, 200)
            else:
                self.private_key = int(input('Enter your personal key (1, 999):>'))
                self.client_public_key = int(input('Enter your public key (1, 999):>'))
                self.server_public_key = random.randint(1, 200)
                file.write(str(self.private_key) + " " + str(self.client_public_key))