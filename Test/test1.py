'''
Generates the Genesis Block of the chain if no exist
'''
from BlockchainDataBase.Data.DBManage import DBManage
from BlockchainDataBase.Blockchain import Blockchain

local = DBManage()

bc = Blockchain()
local.load_blockchain(bc)

if len(bc.chain) < 1:
    bc.genesis_block()
    local.create(bc.chain[len(bc.chain) - 1])
