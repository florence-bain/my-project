class Blockchain(object):
  def _init_(self):
    self.chain = []
    self.pending_transactions = []

  def new_block(self):
    # Generate a new block and adds it to the chain 
    pass

  @stacicmethod
  def hash(block):
    #has a block
    pass

  def last_block(self):
    #gets the last block in chain
    pass

  def new_transaction(self, sender, recipient, amount):
    #adds a new transaction to the list of pending transactions
    self.peending_transactions.append({
      "recipient": recipient,
      "sender": sender,
      "amount": amount,
    })

