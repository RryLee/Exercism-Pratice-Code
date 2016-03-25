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
    def __init__(self, key):
        self.offset = ord(key[0]) - 97

    def encode(self, code):
        secret = ''
        for s in filter_code(code):
            secret += chr(ord(s) + self.offset) if ord(s) + self.offset <= 122 else chr(ord(s) + self.offset - 25)

        return secret
