import json
import os
import time

from web3 import Web3
from web3.auto import w3
import certify4py.utils as Utils
from certify4py.certify_sc_utils import abi as abi_cert
from certify4py.university_abi import abi as abi_univ
from certify4py.chainpoint import ChainPointV2

DEFAULT_GAS_LIMIT = 2000000
VERSION = "v1.0-python"


class Issuer:
    def __init__(self, smart_contract_address,
                 node_host,
                 issuer_address='',
                 issuer_name='',
                 chain_id=1104,
                 hash_type='sha256',
                 contract_type=''):
        self.smart_contract_address = w3.toChecksumAddress(smart_contract_address)
        self.issuer_address = w3.toChecksumAddress(issuer_address) if issuer_address != '' else ''
        self.issuer_name = issuer_name
        self.node_host = node_host
        self.chain_id = chain_id
        self.hash_type = hash_type
        self.contract_type = contract_type
        self.__client = Web3(Web3.HTTPProvider(node_host))

        if contract_type == 'university':
            abi = abi_univ
        else:
            abi = abi_cert
        self.__contract_instance = self.__client.eth.contract(address=self.smart_contract_address, abi=abi)

    def get_pk(self,
               private_key: str = "",
               key_store="",
               passphrase: str = ""):
        pk = private_key
        if private_key == "":
            if os.path.isdir(key_store):
                path = os.path.join(key_store, self.issuer_address + '.json')
                pk = Utils.decrypt_account(passphrase, path)
            elif os.path.isfile(key_store):
                pk = Utils.decrypt_account(passphrase, key_store)
            else:
                raise ValueError("Private key or key store file is required")
        return pk

    def issue(self,
              id: str,
              hash_value: str,
              expire_date: int,
              desc: str,
              private_key: str = "",
              key_store="",
              passphrase: str = "",
              do_hash=False,
              hash_image: str = "",
              hash_json: str = ""
              ):
        pk = self.get_pk(private_key, key_store, passphrase)

        cp = ChainPointV2(self.hash_type)
        cp.add_leaf([hash_value], do_hash=do_hash)
        cp.make_tree()
        # check credit
        if self.get_credit(self.issuer_address) == 0:
            raise ValueError("Not enough credit")

        cert = self.get_certificate(cp.get_merkle_root())

        if cert.isRevoked:  # isRevoked flag
            raise ValueError("Certificate revoked")

        if cert.id > 0:  # id
            raise ValueError("Certificate already registered")

        if self.is_duplicated_cert_num(cert_num=id):
            raise ValueError("Certificate number already registered")

        tx, error = self.__issue_util(hash_value, self.issuer_address, id, expire_date, VERSION, desc, pk,
                                      hash_image, hash_json)
        if error is not None:
            print(error)
            raise RuntimeError(error)
            # insert proof
        proof = cp.get_receipt(0, tx, self.chain_id != 1104)

        return (tx, proof), None

    def __issue_util(self, hash_value, issuer_address, cert_num, expire_date, version, desc, pk,
                     hash_image="", hash_json=""):
        nonce = self.__client.eth.get_transaction_count(self.__client.toChecksumAddress(issuer_address))
        try:
            if self.contract_type == "":
                func = self.__contract_instance.functions.addCertification(hash_value, cert_num, expire_date, version,
                                                                           desc)
            else:
                func = self.__contract_instance.functions.addCertification(hash_value, hash_image, hash_json,
                                                                           cert_num, expire_date, desc)
            tx = func.buildTransaction(
                {'from': issuer_address, 'gasPrice': self.__client.toWei('1000', 'gwei'),
                 'nonce': nonce, 'gas': DEFAULT_GAS_LIMIT})
            signed = self.__client.eth.account.sign_transaction(tx, pk)
            tx_hash = self.__client.eth.send_raw_transaction(signed.rawTransaction)
            tx_res = self.__client.eth.wait_for_transaction_receipt(tx_hash)
            if tx_res.status == 1:
                try:
                    self.write_txid(hash_value, self.__client.toHex(tx_hash), issuer_address, pk)
                except Exception as e:
                    print("Error occurred when sending txid" + str(e))
                return self.__client.toHex(tx_hash), None
            return '', 'Failed on blockchain'
        except Exception as e:
            print(e)
            return '', e

    def write_txid(self, hash_value: str, tx_hash: str, issuer_address, pk):
        nonce = self.__client.eth.get_transaction_count(self.__client.toChecksumAddress(issuer_address))
        func = self.__contract_instance.functions.addTransactionId(hash_value, tx_hash)
        tx = func.buildTransaction(
            {'from': issuer_address, 'gasPrice': self.__client.toWei('1000', 'gwei'),
             'nonce': nonce, 'gas': DEFAULT_GAS_LIMIT})
        signed = self.__client.eth.account.sign_transaction(tx, pk)
        tx_hash2 = self.__client.eth.send_raw_transaction(signed.rawTransaction)
        self.__client.eth.wait_for_transaction_receipt(tx_hash2)

    def revoke(self,
               merkle_root,
               revoker_name,
               private_key: str = "",
               key_store="",
               passphrase: str = ""):
        pk = self.get_pk(private_key, key_store, passphrase)
        # check credit
        if self.get_credit(self.issuer_address) == 0:
            raise ValueError("Not enough credit")

        cert = self.get_certificate(merkle_root)

        if cert.id == 0:
            raise ValueError("Certificate not found")
        if cert.isRevoked:
            raise ValueError("Certificate already revoked")

        tx, error = self.revoke_util(merkle_root, self.issuer_address, revoker_name, pk)
        if error is not None:
            print(error)
            raise RuntimeError(error)

        return tx, None

    def revoke_util(self, merkle_root, revoker_address, revoker_name, pk):
        nonce = self.__client.eth.get_transaction_count(self.__client.toChecksumAddress(revoker_address))

        try:
            func = self.__contract_instance.functions.revoke(merkle_root, revoker_name)
            tx = func.buildTransaction(
                {'from': revoker_address, 'gasPrice': self.__client.toWei('1000', 'gwei'), 'nonce': nonce,
                 'gas': DEFAULT_GAS_LIMIT})
            signed = self.__client.eth.account.sign_transaction(tx, pk)
            tx_hash = self.__client.eth.send_raw_transaction(signed.rawTransaction)
            tx_res = self.__client.eth.wait_for_transaction_receipt(tx_hash)
            if tx_res.status == 1:
                return self.__client.toHex(tx_hash), None
            return '', 'Failed on blockchain'
        except Exception as e:
            print(e)
            return '', e

    def verify_hash(self, hash_value, chainpoint_proof: str):
        proof = json.loads(chainpoint_proof)['proof']
        cp = ChainPointV2(self.hash_type)
        merkle_root = cp.calc_merkle_root(proof, hash_value)
        self.verify_root(merkle_root)

    def verify_root(self, merkle_root):
        cert = self.get_certificate(merkle_root)
        issuer = self.get_issuer(cert.issuer)
        state = 'ISSUED'
        if cert.id == 0:
            raise Exception("Hash not found in smart contract")
        if cert.isRevoked:
            state = 'REVOKED'
        else:
            ts = time.time()
            if 0 < cert.expireDate < ts:
                state = 'EXPIRED'
        result = {
            "cert": cert,
            "issuer": issuer,
            "state": state
        }
        return result

    def get_credit(self, address: str):
        return self.__contract_instance.functions.getCredit(self.__client.toChecksumAddress(address)).call()

    def is_duplicated_cert_num(self, cert_num: str):
        if self.contract_type == '':
            return False
        arr = self.__contract_instance.functions.getCertificationByCertNum(cert_num).call()
        if arr[0] > 0:
            arr2 = self.__contract_instance.functions.getRevokeInfo(arr[2]).call()
            if arr2[1] is True:
                return False
            else:
                return True
        return False

    def get_certificate(self, merkle_root):
        arr = self.__contract_instance.functions.getCertification(merkle_root).call()
        if self.contract_type == "":
            return CertStruct({
                'id': arr[0],
                'certNum': arr[1],
                'hash': arr[2],
                'issuer': arr[3],
                'expireDate': arr[4],
                'createdAt': arr[5],
                'isRevoked': arr[6],
                'version': arr[7],
                'description': arr[8],
                'revokerName': arr[9],
                'revokedAt': arr[10],
                'txid': arr[11]
            })

        arr2 = self.__contract_instance.functions.getRevokeInfo(merkle_root).call()
        return CertStruct({
            'id': arr[0],
            'certNum': arr[1],
            'hash': arr[2],
            'image_hash': arr[3],
            'meta_hash': arr[4],
            'issuer': arr[5],
            'expireDate': arr[6],
            'createdAt': arr[7],
            'description': arr[8],
            'txid': arr[9],
            'isRevoked': arr2[1],
            'revokerName': arr2[3],
            'revokedAt': arr2[5],
        })

    def get_issuer(self, address: str):
        arr = self.__contract_instance.functions.getIssuer(self.__client.toChecksumAddress(address)).call()
        return IssuerStruct({
            'id': arr[0],
            'name': arr[1],
            'regnum': arr[2],
            'description': arr[3],
            'category': arr[4],
            'addr': arr[5],
            'metaDataUrl': arr[6],
            'isActive': arr[7],
            'createdAt': arr[8],
            'updatedAt': arr[9],
        })


class CertStruct:
    id: int
    certNum: str
    hash: str
    issuer: str
    expireDate: int
    createdAt: int
    isRevoked: bool
    version: str
    description: str
    revokerName: str
    revokedAt: int
    txid: str

    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)


class IssuerStruct:
    id: int
    name: str
    regnum: str
    description: str
    category: str
    addr: str
    metaDataUrl: str
    isActive: bool
    createdAt: int
    updatedAt: int

    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)
