'''
Generates the Genesis Block and add two block of data to the chain,
later validate the block to check if is correct.
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

data2 = {"Data2": "dataResult2"}
bc.add_block(data2)
local.create(bc.chain[len(bc.chain) - 1])

bc.print_blocks()
print("\n\r")
bc.validate_chain()
