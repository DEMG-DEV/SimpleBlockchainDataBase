import sqlite3
from BlockchainDataBase.Block import Block


class DBManage:
    def __init__(self, sqlite_file):
        self.conn = sqlite3.connect(sqlite_file)
        self.cursor = self.conn.cursor()

    def createTabe(self):
        try:
            self.cursor.execute("CREATE TABLE blockchain( "
                                "time_stamp DateTime,"
                                "data TEXT, "
                                "previous_hash TEXT, "
                                "nonce int, "
                                "id int PRIMARY KEY, "
                                "hash TEXT)")
            self.conn.commit()
        except:
            pass

    def Create(self, block):
        val = "INSERT INTO blockchain(time_stamp,data,previous_hash,nonce,id,hash) VALUES(\"" + str(
            block.time_stamp) + "\",\"" + str(block.data) + "\",\"" + str(block.previous_hash) + "\"," + str(
            block.nonce) + "," + str(block.index) + ",\"" + str(block.hash) + "\")"

        self.cursor.execute(val)
        self.conn.commit()

    def previousData(self):
        self.cursor.execute("SELECT previous_hash, id FROM blockchain ORDER BY id DESC LIMIT 1")
        value = self.cursor.fetchall()
        return value[0][0], value[0][1]

    def loadBlockchain(self, blockchain):
        self.cursor.execute("SELECT * FROM blockchain")
        values = self.cursor.fetchall()
        for index, values in enumerate(values):
            block = Block()
            block.time_stamp = str(values[0])
            block.data = str(values[1])
            block.previous_hash = str(values[2])
            block.nonce = values[3]
            block.index = values[4]
            block.hash = str(values[5])
            blockchain.chain.append(block)

    def closeDB(self):
        self.conn.close()
