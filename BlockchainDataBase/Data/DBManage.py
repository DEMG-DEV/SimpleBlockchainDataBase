import json
import os
import sqlite3
from BlockchainDataBase.Block import Block


class DBManage:
    def __init__(self):
        self.load_config()
        self.conn = sqlite3.connect(
            self.database_location + self.database_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def load_config(self):
        cwd = os.path.dirname(os.path.realpath(__file__))
        with open(cwd + '\\config.json') as json_data_file:
            data = json.load(json_data_file)

        self.database_name = data['DEFAULT']['DATABASE_NAME']
        self.database_location = os.environ['APPDATA'] + data['DEFAULT']['DATABASE_LOCATION']
        if not os.path.exists(self.database_location):
            os.makedirs(self.database_location)

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
