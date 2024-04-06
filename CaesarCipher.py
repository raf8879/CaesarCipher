class CaesarCipher:

    def __init__(self, step):
        self.step = step

    def encode(self, word):
        s = ''
        for i in word:
            if ord(i) in range(97, 123):
                a = ord(i) + self.step
                if a > 122:
                    a -= 26
                s += chr(a)
            elif ord(i) in range(65, 91):
                a = ord(i) + self.step
                if a > 91:
                    a -= 26
                s += chr(a)
            else:
                s += i
        return s

    def decode(self, word):
        s = ''
        for i in word:
            if ord(i) in range(97, 123):
                a = ord(i) - self.step
                if a < 97:
                    a += 26
                s += chr(a)
            elif ord(i) in range(65, 91):
                a = ord(i) - self.step
                if a < 65:
                    a += 26
                s += chr(a)
            else:
                s += i
        return s