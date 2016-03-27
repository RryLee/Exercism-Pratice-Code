import random
from time import time
from string import ascii_lowercase

def filter_code(code):
    code = code.lower()
    code = filter(lambda s: 'a' <= s <= 'z', code)

    return code

class Caesar:
    def __init__(self):
        pass

    def encode(self, code):
        secret = ''
        for s in filter_code(code):
            secret += chr(ord(s) + 3) if ord(s) + 3 <= 122 else chr(ord(s) - 23)

        return secret

    def decode(self, secret):
        code = ''
        for s in filter_code(secret):
            code += chr(ord(s) - 3) if ord(s) - 3 >= 97 else chr(ord(s) + 119)

        return code


class Cipher:
    def __init__(self, key = None):
        if not key:
            random.seed(time())
            key = ''.join(random.choice(ascii_lowercase) for i in range(100))
        elif not key.isalpha() or not key.islower():
            raise ValueError('Invalid Key')
            
        self.key = key

    def encode(self, code):
        code = filter_code(code)
        key = self.key * (len(code) // len(self.key) + 1)
        return ''.join(chr((ord(k) - 97 + ord(c) - 97) % 26 + 97)
                        for c, k in zip(code, key))

    def decode(self, secret):
        secret = filter_code(secret)
        key = self.key * (len(secret) // len(self.key) + 1)
        return ''.join(chr((ord(c) - ord(k) + 26) % 26 + 97)
                        for c, k in zip(secret, key))
