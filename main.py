import numpy as np
import hashlib
import json

def hashing(data):
    return hashlib.sha256(json.dumps(data).encode()).hexdigest()


class Blockchain:
    def _init_(self):
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.genesis_block()

    def genesis_block(self):
        data = {}
        data['proof'] = 0
        data['previous_hash'] = 0
        self.current_data = data
        self.chain.append(data)
        return self.chain

    def proof_of_work(self):
        proof = 0
        hash = hashing(self.current_data)
        while not (hash.startswith('0' * 3)):
            proof += 1
            self.current_data['proof'] = proof
            hash = hashing(self.current_data)
        return proof

    def add_block(self, data):
        self.current_data = data
        proof = self.proof_of_work()
        self.current_data['proof'] = proof
        previous_hash = hashing(self.chain[-1])
        self.current_data['previous_hash'] = previous_hash
        self.chain.append(self.current_data)
        return self.chain

    # instance of blockchain class


blockchain = Blockchain()

# adding blocks to the blockchain
for i in range(10):
    data = {'transaction': np.random.randint(1, 100)}
    blockchain.add_block(data)

# printing the blockchain
print(blockchain.chain)
