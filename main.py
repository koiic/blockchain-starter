from blockchain import BlockChain

if __name__ == '__main__':
    #Create a BLK object
    bitcoin = BlockChain()
    bitcoin.create_new_block(100, '0', '0')
    print(bitcoin.chain)

    #STAGEONE
    #Create new transactions
    bitcoin.create_new_transaction(120000, "Dan", "Alex")
    bitcoin.create_new_transaction(23000, "Alex", "Bob")
    bitcoin.create_new_transaction(87678, "Bob", "Dan")
    bitcoin.create_new_transaction(678, "Alex", "Dan")

    #createNewBlock, getLastBlock, createNewTransaction, hashBlock, proofOfWork
    last_block = bitcoin.get_last_block()
    previous_block_hash = last_block.get('hash')

    #calculate nonce
    nonce = bitcoin.proof_of_work(previous_block_hash, bitcoin.new_transactions)

    #hash the block
    hash = bitcoin.hash_block(previous_block_hash, bitcoin.new_transactions, nonce)

    #create new block
    bitcoin.create_new_block(nonce, previous_block_hash, hash)

    # STAGE TWO
    # Create new transactions
    bitcoin.create_new_transaction(654567, "Alex", "Dan")
    bitcoin.create_new_transaction(23000, "Chris", "Bob")
    bitcoin.create_new_transaction(87678, "Alice", "Rebecca")

    #createNewBlock, getLastBlock, createNewTransaction, hashBlock, proofOfWork
    last_block = bitcoin.get_last_block()
    previousBlockHash = last_block.get('hash')

    # Calculate nonce
    nonce = bitcoin.proof_of_work(previous_block_hash, bitcoin.new_transactions)

    #Hash the block
    hash = bitcoin.hash_block(previous_block_hash, bitcoin.new_transactions, nonce)

    #Create new block
    bitcoin.create_new_block(nonce, previousBlockHash, hash)

    print(bitcoin)