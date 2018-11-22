'''
Generates the Genesis Block and add one block of data to the chain.
'''

from BlockchainDataBase.Blockchain import Blockchain

bc = Blockchain()

if len(bc.chain) < 1:
    bc.genesis_block()

data = {"Data": "dataResult"}
bc.add_block(data)
bc.print_blocks()
