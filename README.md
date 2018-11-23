# SimpleBlockchainDatabase [![Open Source Helpers](https://www.codetriage.com/demg-dev/simpleblockchaindatabase/badges/users.svg)](https://www.codetriage.com/demg-dev/simpleblockchaindatabase)
In this repository you can found a simple Database based on blockchain technology.

> **IN THIS MOMENT THE DATABASE JUST WORK AS LOCALLY AND ONE DEVICE**

## Version
**1.1.2**

## LICENSE
[MIT License](LICENSE)

## Requirements
Python >= 3.6

## Project structure
```bash
├── BlockchainDataBase
│   ├── Data
│   │   ├── __init__.py
│   │   ├── DBManage.py
│   │   ├── config.json
│   ├── __init__.py
│   ├── Block.py
│   ├── Blockchain.py
├── Test
│   ├── Test1.py
│   ├── Test2.py
│   ├── Test3.py
│   ├── Test4.py
├── LICENSE
├── README.md
├── setup.py
```

## Test
- **Test1.py**, This test just creates the genesis block of the blockchain.
- **Test2.py**, This test add a one block to the blockchain and prints the blocks.
- **Test3.py**, This test add 2 blocks into the blockchain, prints the blocks and validate the blockchain.
- **Test4.py**, This shows all the blocks. 

## Install
From test.pypi.org
```
python -m pip install --index-url https://test.pypi.org/simple/ BlockchainDataBase
```

From official pypi.org
```
python -m pip install BlockchainDataBase
```

## Configuration
On the folder you found a configuration file in a JSON format, if you want to change the folder on the database or database name you do in this file.
```
# The data saves on %APPDATA% directory.
├── BlockchainDataBase
│   ├── Data
│   │   ├── config.json
```
```
config.json

{
  "DEFAULT": {
    "DATABASE_LOCATION": "/blockchain/",
    "DATABASE_NAME": "blockchain_database.bc"
  }
}
```

## Examples
Initialize the Blockchain.
```
from BlockchainDataBase.Blockchain import Blockchain

bc = Blockchain()
```

Add one block into Blockchain.
```
data = {"Data": "dataResult"}
bc.add_block(data)
```

Shows all the blocks in the Blockchain.
```
bc.print_blocks()
```

Validates the blockchain to check if not was corrupted
```
bc.validate_chain()
```
