import datetime
from hashlib import sha256


class Block:
    def __init__(self, data=None, previous_hash=None, index=None):
        '''
        Block of data in the current chain.

        :param data: Data to save in this block inside of chain.
        :param previous_hash: Previous hash in the previous block in the chain.
        :param index: Index of the current block in the chain.
        '''
        self.time_stamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.index = index
        self.hash = self.generate_hash()

    def generate_hash(self):
        '''
        Generates the Hash of the current block in the chain.

        :return: Hash generated of the current block.
        '''
        block_header = str(self.time_stamp) + str(self.data) + str(self.previous_hash) + str(self.nonce) + str(
            self.index)
        block_hash = sha256(block_header.encode())
        return block_hash.hexdigest()

    def print_contents(self):
        '''
        Print data of the current block in the chain.

        :return: Print the data for the user in the current block in the chain.
        '''
        print("timestamp :", self.time_stamp)
        print("data :", self.data)
        print("hash :", self.generate_hash())
        print("previous hash :", self.previous_hash)
        print("index :", self.index)
