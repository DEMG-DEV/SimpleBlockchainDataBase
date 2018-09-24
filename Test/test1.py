'''
Generates the Genesis Block of the chain if no exist
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
