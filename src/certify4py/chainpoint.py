from merkletools import MerkleTools

CHAINPOINT_CONTEXT = 'https://w3id.org/chainpoint/v2'
CHAINPOINT_HASH_TYPES = {'sha224': 'ChainpointSHA224v2',
                         'sha256': 'ChainpointSHA256v2',
                         'sha384': 'ChainpointSHA384v2',
                         'sha512': 'ChainpointSHA512v2',
                         'sha3_224': 'ChainpointSHA3-224v2',
                         'sha3_256': 'ChainpointSHA3-256v2',
                         'sha3_384': 'ChainpointSHA3-384v2',
                         'sha3_512': 'ChainpointSHA3-512v2'}
CHAINPOINT_ANCHOR_TYPES = {
    'corex': 'CorexDataMain',
    'corex_testnet': 'CorexDataTest'}  # , 'eth': 'ETHData'


class ChainPointV2(object):
    """
    Implements chainpoint v2 proof of existence approach
    """

    def __init__(self, hash_type="sha256"):
        self.hash_type = hash_type.lower()
        self.mk = MerkleTools(hash_type)

    '''Wraps merkletools methods'''

    def reset_tree(self):
        self.mk.reset_tree()

    def add_leaf(self, values, do_hash=False):
        self.mk.add_leaf(values, do_hash)

    def get_leaf(self, index):
        return self.mk.get_leaf(index)

    def get_leaf_count(self):
        return self.mk.get_leaf_count()

    def get_tree_ready_state(self):
        return self.mk.get_tree_ready_state()

    def make_tree(self):
        self.mk.make_tree()

    def get_merkle_root(self):
        return self.mk.get_merkle_root()

    def get_proof(self, index):
        return self.mk.get_proof(index)

    def calc_merkle_root(self, proof, hash_value):
        return self.mk.calc_merkle_root(proof, hash_value)

    def validate_proof(self, proof, target_hash, merkle_root):
        return self.mk.validate_proof(proof, target_hash, merkle_root)

    def get_chainpoint_hash_type(self):
        return CHAINPOINT_HASH_TYPES[self.hash_type]

    def get_receipt(self, index, source_id, test_net=False):
        """
        Returns the chainpoint v2 blockchain receipt for specific leaf
        Currently only works for corexchain
        """
        # chain_type = utils.get_chain_type(chain, testnet)
        chain_type = 'corex_testnet' if test_net else 'corex'
        if chain_type is not None and self.get_tree_ready_state():
            return {
                "context": CHAINPOINT_CONTEXT,
                "type": self.get_chainpoint_hash_type(),
                "targetHash": self.get_leaf(index),
                "merkleRoot": self.get_merkle_root(),
                "proof": self.get_proof(index),
                "anchors": [
                    {
                        "type": CHAINPOINT_ANCHOR_TYPES[chain_type],
                        "sourceId": source_id
                    }
                ]
            }
        else:
            return None
