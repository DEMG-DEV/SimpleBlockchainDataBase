'''
Generates the Genesis Block and add one block of data to the chain.
'''

from BlockchainDataBase.Data.DBManage import DBManage
from BlockchainDataBase.Blockchain import Blockchain

local = DBManage()

bc = Blockchain()
local.load_blockchain(bc)

if len(bc.chain) < 1:
    bc.genesis_block()
    local.create(bc.chain[len(bc.chain) - 1])

data = {"Data": "dataResult"}
bc.add_block(data)
local.create(bc.chain[len(bc.chain) - 1])
bc.print_blocks()
