import sqlite3
from BlockchainDataBase.Block import Block


class DBManage:
    def __init__(self):
        self.conn = sqlite3.connect("blockchain_database.bc")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
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

    def create(self, block):
        val = "INSERT INTO blockchain(time_stamp,data,previous_hash,nonce,id,hash) VALUES(\"" + str(
            block.time_stamp) + "\",\"" + str(block.data) + "\",\"" + str(block.previous_hash) + "\"," + str(
            block.nonce) + "," + str(block.index) + ",\"" + str(block.hash) + "\")"

        self.cursor.execute(val)
        self.conn.commit()

    def previous_data(self):
        self.cursor.execute(
            "SELECT previous_hash, id FROM blockchain ORDER BY id DESC LIMIT 1")
        value = self.cursor.fetchall()
        return value[0][0], value[0][1]

    def load_blockchain(self, blockchain):
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

    def close_db(self):
        self.conn.close()
