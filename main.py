import hashlib

from block import Block
from blockchain import BlockChain
from client import Client
from transaction import Transaction


def display_transaction(transaction):
    dict = transaction.to_dict()
    print("sender: " + dict['sender'])
    print('-----')
    print("recipient: " + dict['recipient'])
    print('-----')
    print("value: " + str(dict['value']))
    print('-----')
    print("time: " + str(dict['time']))
    print('-----')


transactions = []
last_block_hash = ''
TPCoins = []
last_transaction_index = 0


def dump_blockchain(self):
    print("Number of blocks in the chain: " + str(len(self)))
    for x in range(len(TPCoins)):
        block_temp = TPCoins[x]
        print("block # " + str(x))
        for transaction in block_temp.verified_transactions:
            display_transaction(transaction)
            print('-----------------------------')
        print("===================================================")


# generate hexdeimal by hashing message for mining
def sha256(message):
    return hashlib.sha256(message.encode('ascii')).hexdigest()


def mine(message, difficulty=1):
    assert difficulty >=1
    prefix = '1' * difficulty
    for i in range(1000):
        digest = sha256(str(hash(message)) + str(i))
        if digest.startswith(prefix):
            print('after ' + str(i) + ' iterations found nonce: ' + digest)
            return digest



if __name__ == '__main__':
    # #Create a BLK object
    # bitcoin = BlockChain()
    # bitcoin.create_new_block(100, '0', '0')
    # print(bitcoin.chain)
    #
    # #STAGEONE
    # #Create new transactions
    # bitcoin.create_new_transaction(120000, "Dan", "Alex")
    # bitcoin.create_new_transaction(23000, "Alex", "Bob")
    # bitcoin.create_new_transaction(87678, "Bob", "Dan")
    # bitcoin.create_new_transaction(678, "Alex", "Dan")
    #
    # #createNewBlock, getLastBlock, createNewTransaction, hashBlock, proofOfWork
    # last_block = bitcoin.get_last_block()
    # previous_block_hash = last_block.get('hash')
    #
    # #calculate nonce
    # nonce = bitcoin.proof_of_work(previous_block_hash, bitcoin.new_transactions)
    #
    # #hash the block
    # hash = bitcoin.hash_block(previous_block_hash, bitcoin.new_transactions, nonce)
    #
    # #create new block
    # bitcoin.create_new_block(nonce, previous_block_hash, hash)
    #
    # # STAGE TWO
    # # Create new transactions
    # bitcoin.create_new_transaction(654567, "Alex", "Dan")
    # bitcoin.create_new_transaction(23000, "Chris", "Bob")
    # bitcoin.create_new_transaction(87678, "Alice", "Rebecca")
    #
    # #createNewBlock, getLastBlock, createNewTransaction, hashBlock, proofOfWork
    # last_block = bitcoin.get_last_block()
    # previousBlockHash = last_block.get('hash')
    #
    # # Calculate nonce
    # nonce = bitcoin.proof_of_work(previous_block_hash, bitcoin.new_transactions)
    #
    # #Hash the block
    # hash = bitcoin.hash_block(previous_block_hash, bitcoin.new_transactions, nonce)
    #
    # #Create new block
    # bitcoin.create_new_block(nonce, previousBlockHash, hash)
    #
    # print(bitcoin)

    # Testing client
    Ibrahim = Client()
    Ramesh = Client()
    Seema = Client()
    Vijay = Client()
    print(Ibrahim.identity)

    #Testing transaction
    t1 = Transaction(Ibrahim, Ramesh.identity, 5.0)
    t1.sign_transaction()
    transactions.append(t1)

    t2 = Transaction(Ibrahim, Seema.identity, 6.0)
    t2.sign_transaction()
    transactions.append(t2)

    t3 = Transaction(Ramesh, Vijay.identity, 2.0)
    t3.sign_transaction()
    transactions.append(t3)

    t4 = Transaction(Seema, Ramesh.identity, 4.0)
    t4.sign_transaction()
    transactions.append(t4)

    t5 = Transaction(Vijay, Seema.identity, 7.0)
    t5.sign_transaction()
    transactions.append(t5)

    t6 = Transaction(Ramesh, Seema.identity, 3.0)
    t6.sign_transaction()
    transactions.append(t6)

    t7 = Transaction(Seema, Ibrahim.identity, 8.0)
    t7.sign_transaction()
    transactions.append(t7)

    t8 = Transaction(Seema, Ramesh.identity, 1.0)
    t8.sign_transaction()
    transactions.append(t8)

    t9 = Transaction(Vijay, Ibrahim.identity,5.0)
    t9.sign_transaction()
    transactions.append(t9)

    t10 = Transaction(Vijay, Ramesh.identity, 3.0)
    t10.sign_transaction()
    transactions.append(t10)

    # for transaction in transactions:
    #     display_transaction(transaction)
    #     print('-----------------------------')

    t0 = Transaction(
        "Genesis",
        Ibrahim.identity,
        500.0
    )
    # #Tesing Block
    block0 = Block()
    block0.previous_block_hash = None
    block0.Nonce = None
    block0.verified_transactions.append(t0)
    last_transaction_index += 1
    digest = hash(block0)
    last_block_hash = digest
    TPCoins.append(block0)
    dump_blockchain(TPCoins)


    # print(last_block_hash, 'hash')

    #Testing mining function
    mine('test message', 2)
    block1 = Block()
    print("i got here", block1)

    for i in range(3):
        temp_transaction = transactions[last_transaction_index]
        #validate transactions
        #if valid
        block1.verified_transactions.append(temp_transaction)
        last_transaction_index += 1
    block1.previous_block_hash = last_block_hash
    block1.Nonce = mine(block1, 2)
    digest = hash(block1)
    TPCoins.append(block1)
    last_block_hash = digest

    # Miner 2 adds a block
    block2 = Block()
    for i in range(3):
        temp_transaction = transactions[last_transaction_index]
        # validate transaction
        # if valid
        block2.verified_transactions.append(temp_transaction)
        last_transaction_index += 1
    block2.previous_block_hash = last_block_hash
    block2.Nonce = mine(block2, 2)
    digest = hash(block2)
    TPCoins.append(block2)
    last_block_hash = digest

    # Miner 3 adds a block
    block3 = Block()
    for i in range(3):
        temp_transaction = transactions[last_transaction_index]
        # display_transaction (temp_transaction)
        # validate transaction
        # if valid
        block3.verified_transactions.append(temp_transaction)
        last_transaction_index += 1

    block3.previous_block_hash = last_block_hash
    block3.Nonce = mine(block3, 2)
    digest = hash(block3)

    TPCoins.append(block3)
    last_block_hash = digest

    dump_blockchain(TPCoins)
