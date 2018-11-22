'''
Print all the current blocks.
'''

from BlockchainDataBase.Blockchain import Blockchain


bc = Blockchain()

if len(bc.chain) < 1:
    bc.genesis_block()

bc.print_blocks()