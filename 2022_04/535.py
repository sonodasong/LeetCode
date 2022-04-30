class Codec:

    def __init__(self):
        self.l = []
        self.base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        d = {}
        for i, c in enumerate(self.base):
            d[c] = i
        self.d = d

    def encode(self, longUrl: str) -> str:
        base = self.base
        self.l.append(longUrl)
        i = len(self.l)
        a = ''
        while i > 0:
            a += base[i % 62]
            i //= 62
        return 'http://' + a

    def decode(self, shortUrl: str) -> str:
        d = self.d
        a = shortUrl[7:]
        i = 0
        for a in a:
            i *= 10
            i += d[a]
        return self.l[i - 1]

if __name__ == '__main__':
    codec = Codec()
    print(codec.decode(codec.encode(longUrl='https://leetcode.com/problems/design-tinyurl')))
