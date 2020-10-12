import hashlib

def decoder(word):
    word = word.encode('utf-8')
    md5 = hashlib.md5(word).hexdigest()
    return md5
