from BlockchainDataBase.Block import Block
from BlockchainDataBase.Data.DBManage import DBManage


class Blockchain:
    def __init__(self):
        '''
        Initialize the chain.
        '''
        self.chain = []
        self.data_base = DBManage()
        self.data_base.load_blockchain(self)

    def genesis_block(self):
        '''
        Generates the genesis block who initialize the chain.

        :return: The genesis block for the new chain.
        '''
        data = []
        genesis_block = Block(data, "0", 0)
        genesis_block.generate_hash()
        self.chain.append(genesis_block)
        self.data_base.create(self.chain[len(self.chain) - 1])

    def add_block(self, data):
        previous_hash = (self.chain[len(self.chain) - 1]).hash
        new_block = Block(data, previous_hash, (self.chain[len(self.chain) - 1]).index + 1)
        new_block.generate_hash()
        proof = self.proof_of_work(new_block)
        self.chain.append(new_block)
        self.data_base.create(self.chain[len(self.chain) - 1])
        return proof, new_block

    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_contents()

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.generate_hash():
                print("The current hash of the block does not equal the generated hash of the block.")
                return False
            if current.previous_hash != previous.generate_hash():
                print("The previous block's hash does not equal the previous hash value stored in the current block.")
                return False
        print("Hash is Valid")
        return True

    def proof_of_work(self, block, difficulty=2):
        proof = block.generate_hash()
        while proof[:difficulty] != '0' * difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        block.nonce = 0
        return proof
