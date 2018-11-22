'''
Generates the Genesis Block of the chain if no exist
'''
from BlockchainDataBase.Blockchain import Blockchain

bc = Blockchain()

if len(bc.chain) < 1:
    bc.genesis_block()
