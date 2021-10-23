import json

from datetime import datetime
from hashlib import sha256


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        # create genesis block
        print("Creating genesis block")
        self.new_block()

    def last_block(self):
        # returns the last block in a chain
        return self.chain[-1] if self.chain else None

    def new_block(self, previous_hash=None):
        block = {
            'index': len(self.chain),
            'timestamp': datetime.utcnow().isoformat(),
            'transactions': self.pending_transactions,
            'previous_hash': previous_hash,
        }
        # get the hash of this new block and add to the block
        block_hash = self.hash(block)
        block["hash"] = block_hash

        # reset the list of of pending transactions
        self.pending_transactions = []
        # add block to chain
        self.chain.append(block)
        # Generate a new block and adds it to the chain

        print(f"Created block {block['index']}")
        return block

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    def new_transaction(self, sender, recipient, amount):
        # adds a new transaction to the list of pending transactions
        self.pending_transactions.append({
            "recipient": recipient,
            "sender": sender,
            "amount": amount,
        })
