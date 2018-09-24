'''
Generates the Genesis Block and add one block of data to the chain.
'''

from BlockchainDataBase.Data.DBManage import DBManage
from BlockchainDataBase.Blockchain import Blockchain

local = DBManage("database.bc")
local.createTabe()

bc = Blockchain()
local.loadBlockchain(bc)

if len(bc.chain) < 1:
    bc.genesis_block()
    local.Create(bc.chain[len(bc.chain) - 1])

data = {"Data": "dataResult"}
bc.add_block(data)
local.Create(bc.chain[len(bc.chain) - 1])
bc.print_blocks()
