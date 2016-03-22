CHUNK_SIZE = 5

def encode(code):
    secret = ''
    for s in filter(lambda x: 'a' <= x <= 'z' or '0' <= x <= '9', code.lower()):
        if not s.isdigit():
            secret += chr(219 - ord(s))
        else:
            secret += s

    return ' '.join([secret[i:i+CHUNK_SIZE] for i in range(0, len(secret), CHUNK_SIZE)])

def decode(secret):
    code = ''
    for s in filter(lambda x: 'a' <= x <= 'z' or '0' <= x <= '9', secret):
        if s.isdigit():
            code += s
        else:
            code += chr(219 - ord(s))
    return code
