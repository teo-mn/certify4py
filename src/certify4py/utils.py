import hashlib
import json
import os
import random
import shutil
import string
import tempfile

from web3.auto import w3


def random_passphrase(length=8):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols
    temp = random.sample(all, length)
    return "".join(temp)


def decrypt_account(passphrase: str, path: str):
    from web3.auto import w3
    with open(path) as keyfile:
        encrypted_key = keyfile.read()
        private_key = w3.eth.account.decrypt(encrypted_key, passphrase)
        return w3.toHex(private_key)


def calc_hash(file):
    with open(file, 'rb') as cert:
        byte_val = cert.read()
        hash_str = hashlib.sha256(byte_val).hexdigest()
    return hash_str


def calc_hash_str(str_val: str):
    hash_str = hashlib.sha256(str_val.encode('utf-8')).hexdigest()
    return hash_str


def create_temporary_copy(path):
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, 'temp_file_name')
    shutil.copy2(path, temp_path)
    return temp_path


def generate_account(key_store_dir_path: str, verbose=False):
    acc = w3.eth.account.create()
    passphrase = random_passphrase(20)
    keystore = acc.encrypt(passphrase)
    with open(os.path.join(key_store_dir_path, acc.address + '.json'), 'w') as outfile:
        json.dump(keystore, outfile)

    if verbose:
        print("New address generated: ", acc.address)

    return acc.address, passphrase
