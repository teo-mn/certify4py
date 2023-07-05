# import json

from web3 import Web3

abi = [
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_hash",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_certNum",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "_expireDate",
                "type": "uint256"
            },
            {
                "internalType": "string",
                "name": "_version",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_desc",
                "type": "string"
            }
        ],
        "name": "addCertification",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_hash",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_txid",
                "type": "string"
            }
        ],
        "name": "addTransactionId",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "name": "certifications",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            },
            {
                "internalType": "string",
                "name": "certNum",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "hash",
                "type": "string"
            },
            {
                "internalType": "address",
                "name": "issuer",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "expireDate",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "createdAt",
                "type": "uint256"
            },
            {
                "internalType": "bool",
                "name": "isRevoked",
                "type": "bool"
            },
            {
                "internalType": "string",
                "name": "version",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "description",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "revokerName",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "revokedAt",
                "type": "uint256"
            },
            {
                "internalType": "string",
                "name": "txid",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "addr",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "credit",
                "type": "uint256"
            }
        ],
        "name": "chargeCredit",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "creditAddress",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "name": "credits",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "hash",
                "type": "string"
            }
        ],
        "name": "getCertification",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "id",
                        "type": "uint256"
                    },
                    {
                        "internalType": "string",
                        "name": "certNum",
                        "type": "string"
                    },
                    {
                        "internalType": "string",
                        "name": "hash",
                        "type": "string"
                    },
                    {
                        "internalType": "address",
                        "name": "issuer",
                        "type": "address"
                    },
                    {
                        "internalType": "uint256",
                        "name": "expireDate",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "createdAt",
                        "type": "uint256"
                    },
                    {
                        "internalType": "bool",
                        "name": "isRevoked",
                        "type": "bool"
                    },
                    {
                        "internalType": "string",
                        "name": "version",
                        "type": "string"
                    },
                    {
                        "internalType": "string",
                        "name": "description",
                        "type": "string"
                    },
                    {
                        "internalType": "string",
                        "name": "revokerName",
                        "type": "string"
                    },
                    {
                        "internalType": "uint256",
                        "name": "revokedAt",
                        "type": "uint256"
                    },
                    {
                        "internalType": "string",
                        "name": "txid",
                        "type": "string"
                    }
                ],
                "internalType": "struct CertificationRegistration.Certification",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "certNum",
                "type": "string"
            }
        ],
        "name": "getCertificationByCertNum",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "id",
                        "type": "uint256"
                    },
                    {
                        "internalType": "string",
                        "name": "certNum",
                        "type": "string"
                    },
                    {
                        "internalType": "string",
                        "name": "hash",
                        "type": "string"
                    },
                    {
                        "internalType": "address",
                        "name": "issuer",
                        "type": "address"
                    },
                    {
                        "internalType": "uint256",
                        "name": "expireDate",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "createdAt",
                        "type": "uint256"
                    },
                    {
                        "internalType": "bool",
                        "name": "isRevoked",
                        "type": "bool"
                    },
                    {
                        "internalType": "string",
                        "name": "version",
                        "type": "string"
                    },
                    {
                        "internalType": "string",
                        "name": "description",
                        "type": "string"
                    },
                    {
                        "internalType": "string",
                        "name": "revokerName",
                        "type": "string"
                    },
                    {
                        "internalType": "uint256",
                        "name": "revokedAt",
                        "type": "uint256"
                    },
                    {
                        "internalType": "string",
                        "name": "txid",
                        "type": "string"
                    }
                ],
                "internalType": "struct CertificationRegistration.Certification",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "ID",
                "type": "uint256"
            }
        ],
        "name": "getCertificationByID",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "id",
                        "type": "uint256"
                    },
                    {
                        "internalType": "string",
                        "name": "certNum",
                        "type": "string"
                    },
                    {
                        "internalType": "string",
                        "name": "hash",
                        "type": "string"
                    },
                    {
                        "internalType": "address",
                        "name": "issuer",
                        "type": "address"
                    },
                    {
                        "internalType": "uint256",
                        "name": "expireDate",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "createdAt",
                        "type": "uint256"
                    },
                    {
                        "internalType": "bool",
                        "name": "isRevoked",
                        "type": "bool"
                    },
                    {
                        "internalType": "string",
                        "name": "version",
                        "type": "string"
                    },
                    {
                        "internalType": "string",
                        "name": "description",
                        "type": "string"
                    },
                    {
                        "internalType": "string",
                        "name": "revokerName",
                        "type": "string"
                    },
                    {
                        "internalType": "uint256",
                        "name": "revokedAt",
                        "type": "uint256"
                    },
                    {
                        "internalType": "string",
                        "name": "txid",
                        "type": "string"
                    }
                ],
                "internalType": "struct CertificationRegistration.Certification",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "addr",
                "type": "address"
            }
        ],
        "name": "getCredit",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "issuer",
                "type": "address"
            }
        ],
        "name": "getIssuer",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "id",
                        "type": "uint256"
                    },
                    {
                        "internalType": "string",
                        "name": "name",
                        "type": "string"
                    },
                    {
                        "internalType": "string",
                        "name": "regnum",
                        "type": "string"
                    },
                    {
                        "internalType": "string",
                        "name": "description",
                        "type": "string"
                    },
                    {
                        "internalType": "string",
                        "name": "category",
                        "type": "string"
                    },
                    {
                        "internalType": "address",
                        "name": "addr",
                        "type": "address"
                    },
                    {
                        "internalType": "string",
                        "name": "metaDataUrl",
                        "type": "string"
                    },
                    {
                        "internalType": "bool",
                        "name": "isActive",
                        "type": "bool"
                    },
                    {
                        "internalType": "uint256",
                        "name": "createdAt",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "updatedAt",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct SharedStructs.Issuer",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "id",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "initialize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "issuerRegistrationAddress",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "name": "mapByCertNum",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            },
            {
                "internalType": "string",
                "name": "certNum",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "hash",
                "type": "string"
            },
            {
                "internalType": "address",
                "name": "issuer",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "expireDate",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "createdAt",
                "type": "uint256"
            },
            {
                "internalType": "bool",
                "name": "isRevoked",
                "type": "bool"
            },
            {
                "internalType": "string",
                "name": "version",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "description",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "revokerName",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "revokedAt",
                "type": "uint256"
            },
            {
                "internalType": "string",
                "name": "txid",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "name": "mapById",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            },
            {
                "internalType": "string",
                "name": "certNum",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "hash",
                "type": "string"
            },
            {
                "internalType": "address",
                "name": "issuer",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "expireDate",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "createdAt",
                "type": "uint256"
            },
            {
                "internalType": "bool",
                "name": "isRevoked",
                "type": "bool"
            },
            {
                "internalType": "string",
                "name": "version",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "description",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "revokerName",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "revokedAt",
                "type": "uint256"
            },
            {
                "internalType": "string",
                "name": "txid",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "hash",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "revokerName",
                "type": "string"
            }
        ],
        "name": "revoke",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "ID",
                "type": "uint256"
            },
            {
                "internalType": "string",
                "name": "revokerName",
                "type": "string"
            }
        ],
        "name": "revokeById",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_issuerRegistrationAddress",
                "type": "address"
            }
        ],
        "name": "setIssuerRegistrationAddress",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

DEFAULT_GAS_LIMIT = 2000000


def add_certification(hash_str: str, cert_num: str, expire_date: int, version: str, desc: str, node_url: str,
                      address: str, contract_address: str, pk: str):
    client = Web3(Web3.HTTPProvider(node_url))
    contract_instance = client.eth.contract(address=contract_address, abi=abi)
    nonce = client.eth.get_transaction_count(client.toChecksumAddress(address))

    try:
        func = contract_instance.functions.addCertification(hash_str, cert_num, expire_date, version, desc)
        tx = func.buildTransaction(
            {'from': address, 'gasPrice': client.toWei('1000', 'gwei'), 'nonce': nonce, 'gas': DEFAULT_GAS_LIMIT})
        signed = client.eth.account.sign_transaction(tx, pk)
        tx_hash = client.eth.send_raw_transaction(signed.rawTransaction)
        tx_res = client.eth.wait_for_transaction_receipt(tx_hash)
        if tx_res.status == 1:
            return client.toHex(tx_hash), None
        return '', 'Failed on blockchain'
    except Exception as e:
        print(e)
        return '', e


def revoke_certification(hash_str: str, revoker_name: str, node_url: str, contract_address: str, address: str, pk: str):
    client = Web3(Web3.HTTPProvider(node_url))
    contract_instance = client.eth.contract(address=contract_address, abi=abi)
    nonce = client.eth.get_transaction_count(client.toChecksumAddress(address))

    try:
        func = contract_instance.functions.revoke(hash_str, revoker_name)
        tx = func.buildTransaction(
            {'from': address, 'gasPrice': client.toWei('1000', 'gwei'), 'nonce': nonce, 'gas': DEFAULT_GAS_LIMIT})
        signed = client.eth.account.sign_transaction(tx, pk)
        tx_hash = client.eth.send_raw_transaction(signed.rawTransaction)
        tx_res = client.eth.wait_for_transaction_receipt(tx_hash)
        if tx_res.status == 1:
            return client.toHex(tx_hash), None
        return '', 'Failed on blockchain'
    except Exception as e:
        print(e)
        return '', e


def revoke_certification_by_id(cert_id: int, revoker_name: str, node_url: str, contract_address: str, address: str,
                               pk: str):
    client = Web3(Web3.HTTPProvider(node_url))
    # f = open('abi.json')
    # abi = json.load(f)
    contract_instance = client.eth.contract(address=contract_address, abi=abi)
    nonce = client.eth.get_transaction_count(client.toChecksumAddress(address))

    try:
        func = contract_instance.functions.revokeById(cert_id, revoker_name)
        tx = func.buildTransaction(
            {'from': address, 'gasPrice': client.toWei('1000', 'gwei'), 'nonce': nonce, 'gas': DEFAULT_GAS_LIMIT})
        signed = client.eth.account.sign_transaction(tx, pk)
        tx_hash = client.eth.send_raw_transaction(signed.rawTransaction)
        tx_res = client.eth.wait_for_transaction_receipt(tx_hash)
        if tx_res.status == 1:
            return client.toHex(tx_hash), None
        return '', 'Failed on blockchain'
    except Exception as e:
        print(e)
        return '', e


def charge_credit(address: str, credit: int, owner_address, owner_pk, node_url, contract_address):
    client = Web3(Web3.HTTPProvider(node_url))
    # f = open('abi.json')
    # abi = json.load(f)
    contract_instance = client.eth.contract(address=contract_address, abi=abi)
    nonce = client.eth.get_transaction_count(client.toChecksumAddress(owner_address))

    try:
        func = contract_instance.functions.chargeCredit(client.toChecksumAddress(address), credit)
        tx = func.buildTransaction(
            {'from': address, 'gasPrice': client.toWei('1000', 'gwei'), 'nonce': nonce, 'gas': DEFAULT_GAS_LIMIT})
        signed = client.eth.account.sign_transaction(tx, owner_pk)
        tx_hash = client.eth.send_raw_transaction(signed.rawTransaction)
        tx_res = client.eth.wait_for_transaction_receipt(tx_hash)
        if tx_res.status == 1:
            return client.toHex(tx_hash), None
        return '', 'Failed on blockchain'
    except Exception as e:
        print(e)
        return '', e


def get_credit(address: str, contract_address, node_url):
    client = Web3(Web3.HTTPProvider(node_url))
    contract_instance = client.eth.contract(address=contract_address, abi=abi)

    return contract_instance.functions.getCredit(
        client.toChecksumAddress(address)).call()


def get_certificate(hash_str: str, contract_address, node_url):
    client = Web3(Web3.HTTPProvider(node_url))
    contract_instance = client.eth.contract(address=contract_address, abi=abi)
    return contract_instance.functions.getCertification(hash_str).call()
