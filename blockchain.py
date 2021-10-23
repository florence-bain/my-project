import json
import random

from datetime import datetime
from hashlib import sha256


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        # create genesis block
        print("Creating genesis block")
        self.chain.append(self.new_block())

    def new_block(self):
        block = {
            'index': len(self.chain),
            'timestamp': datetime.utcnow().isoformat(),
            'transactions': self.pending_transactions,
            'previous_hash': self.last_block["hash"] if self.last_block else None,
            "nonce": format(random.getrandbits(64), "x"),
        }
        # get the hash of this new block and add to the block
        block_hash = self.hash(block)
        block["hash"] = block_hash

        # reset the list of of pending transactions
        self.pending_transactions = []
        # add block to chain
        # removed self.chain.append(block) to ensure no invalid blocks are added
        # Generate a new block and adds it to the chain

        return block

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # returns the last block in a chain
        return self.chain[-1] if self.chain else None

    # def new_transaction(self, sender, recipient, amount):
    #     # adds a new transaction to the list of pending transactions
    #     self.pending_transactions.append({
    #         "recipient": recipient,
    #         "sender": sender,
    #         "amount": amount,
    #     })
    # method not needed at this time

    @staticmethod
    def valid_block(block):
        return block["hash"].startswith("0000")

    def proof_of_work(self):
        while True:
            new_block = self.new_block()
            if self.valid_block(new_block):
                break

            self.chain.append(new_block)
            print("Found a new block: ", new_block)
