import binascii
import datetime
from collections import OrderedDict

from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5


class Transaction:

    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity
        return OrderedDict({
            'sender': identity,
            'recipient': self.recipient,
            'value': self.value,
            'time': self.time
        })

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        hash = SHA.new(str(self.to_dict()).encode('utf-8'))
        return binascii.hexlify(signer.sign(hash)).decode('ascii')

    def __str__(self):
        return f'{self.sender} - {self.recipient} - {self.value}'