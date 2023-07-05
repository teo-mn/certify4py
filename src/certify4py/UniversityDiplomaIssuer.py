import json
import os

from pdfrw import PdfReader

import certify4py.pdf as pdf_utils
import certify4py.utils as Utils
from certify4py.Issuer import Issuer
from certify4py.json_utils import json_wrap

VERSION = 'v1.0-python-university'


class UniversityDiplomaIssuer(Issuer):
    def __init__(self, smart_contract_address,
                 node_host,
                 issuer_address='',
                 issuer_name='',
                 chain_id=1104,
                 hash_type='sha256'):
        super(UniversityDiplomaIssuer, self).__init__(smart_contract_address,
                                                      node_host, issuer_address,
                                                      issuer_name,
                                                      chain_id,
                                                      hash_type,
                                                      contract_type='university')

    def issue_pdf(self,
                  id: str,
                  source_file_path: str,
                  destination_file_path: str,
                  meta_data: object,
                  expire_date: int,
                  desc: str,
                  additional_info: str,
                  private_key: str = "",
                  key_store="",
                  passphrase: str = ""):

        """
        Issues PDF hash value to the TEO blockchain.
        Params:
        id: Certificate or Diploma number
        source_file_path: Path to pdf that's hash value will be written on blockchain.
        destination_file_path: Path to output PDF file.
        meta_data: Metadata of diploma. See the object structure on README.
        expire_date: Timestamp of expiration. If None, no expiration.
        additional_info: Some description.
        private_key: Blockchain private key.
        key_store: If private_key is None, key_store must be passed.
        passphrase: if key_store is provided, passphrase must be passed.
        """
        verifymn = {
            "issuer": {
                "name": self.issuer_name,
                "address": self.issuer_address
            },
            "info": {
                "name": self.issuer_name,
                "desc": desc,
                "cerNum": id,
                "additionalInfo": additional_info
            },
            "version": VERSION,
            "blockchain": {
                "network": "CorexMain" if self.chain_id == 1104 else "CorexTest",
                "smartContractAddress": self.smart_contract_address
            }
        }

        # validation
        if not os.path.exists(source_file_path) or not os.path.isfile(source_file_path):
            raise ValueError('Source path should be valid')

        if os.path.isdir(destination_file_path):
            raise ValueError('Destination path already exists')

        pdf_utils.add_metadata(source_file_path, destination_file_path, verifymn=json.dumps(verifymn))
        hash_image = Utils.calc_hash(destination_file_path)
        verifymn['univ_meta'] = meta_data
        pdf_utils.add_metadata(source_file_path, destination_file_path, verifymn=json.dumps(verifymn))
        hash_val = Utils.calc_hash(destination_file_path)
        meta_str = json_wrap(meta_data)
        hash_meta = Utils.calc_hash_str(meta_str)
        (tx, proof), error = self.issue(id, hash_val, expire_date, desc, private_key, key_store, passphrase,
                                        hash_image=hash_image, hash_json=hash_meta)
        return tx, error

    def revoke_pdf(self,
                   file_path: str,
                   revoker_name: str,
                   private_key: str = "",
                   key_store="",
                   passphrase: str = ""
                   ):
        # validation
        if not os.path.exists(file_path) or not os.path.isfile(file_path):
            raise ValueError('Source path should be valid')
        hash_val = Utils.calc_hash(file_path)
        return self.revoke(hash_val.lower(), revoker_name, private_key, key_store, passphrase)

    def verify_pdf(self, file_path):
        hash_val = Utils.calc_hash(file_path)
        pdf = PdfReader(file_path)
        metadata = pdf.Info.get('/verifymn')
        result = self.verify_root(hash_val.lower())
        result['metadata'] = metadata
        return result
