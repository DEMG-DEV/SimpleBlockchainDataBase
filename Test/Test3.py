'''
Generates the Genesis Block and add two block of data to the chain,
later validate the block to check if is correct.
'''

from BlockchainDataBase.Blockchain import Blockchain

bc = Blockchain()

if len(bc.chain) < 1:
    bc.genesis_block()

data = {"Data": "dataResult"}
bc.add_block(data)

data2 = {"Data2": "dataResult2"}
bc.add_block(data2)

bc.print_blocks()
print("\n\r")
bc.validate_chain()
