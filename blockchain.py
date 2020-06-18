import datetime
import _sha256
import hashlib


class BlockChain():
    chain = []
    new_transactions = []

    def create_new_block(self, nonce, previous_block_hash, hash):
        new_block = dict(
            index=len(self.chain) + 1,
            time_stamp=datetime.datetime.now(),
            transactions=self.new_transactions,
            nonce=nonce,
            hash=hash,
            previous_block_hash=previous_block_hash
        )
        self.chain.append(new_block);
        self.new_transactions = []
        return new_block

    def get_last_block(self):
        return self.chain[-1] if self.chain else None

    def create_new_transaction(self, amount, sender, recipient):
        new_transaction = {
            amount: amount,
            sender: sender,
            recipient: recipient
        }
        self.new_transactions.append(new_transaction)
        return self.get_last_block()['index'] + 1 if self.chain else None

    def hash_block(self, previous_block_hash, current_block_data, nonce):
        data_as_string = f'{previous_block_hash}{str(nonce)}{str(current_block_data)}'
        hash = hashlib.sha256(data_as_string.encode()).hexdigest()
        # print(hash[0:4])
        return hash

    def proof_of_work(self, previous_block_hash, current_block_data):
        nonce = 0
        hash = self.hash_block(previous_block_hash, current_block_data, nonce)
        while hash[0:4] != '0000':
            nonce += 1
            hash = self.hash_block(previous_block_hash, current_block_data, nonce)
        return nonce

    def __str__(self):
        return f'chain : {self.chain}, transaction : {self.new_transactions}'
