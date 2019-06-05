from datetime import datetime
import hashlib as hasher

import unittest


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def __str__(self):
        return 'Block #{}'.format(self.index)

    def hash_block(self):
        sha = hasher.sha256()
        seq = (str(x) for x in (
            self.index, self.timestamp, self.data, self.previous_hash))
        sha.update(''.join(seq).encode('utf-8'))
        return sha.hexdigest()


def make_genesis_block():
    """Make the first block in a block-chain."""
    block = Block(index=0,
                  timestamp=datetime.now(),
                  data="Genesis Block",
                  previous_hash="0")
    return block


def next_block(last_block, data=''):
    """Return next block in a block chain."""
    idx = last_block.index + 1
    block = Block(index=idx,
                  timestamp=datetime.now(),
                  data='{}{}'.format(data, idx),
                  previous_hash=last_block.hash)
    return block


class TestBlockChain(unittest.TestCase):

    def test_chain(self):
        """Test creating chain of 20 blocks."""
        blockchain = [make_genesis_block()]
        prev_block = blockchain[0]
        for _ in range(0, 20):
            block = next_block(prev_block, data='some data here')
            blockchain.append(block)
            prev_block = block
            print('{} added to blockchain'.format(block))
            print('Hash: {}\n'.format(block.hash))

        # Assert that a blockchain of length 20 was created
        self.assertTrue(len(blockchain), 20)


if __name__ == '__main__':
    unittest.main()
