class Ecc:
    def __init__(self):
        pass
    
    def inverseModulo(self, a=2, p=5):
        gcd, st1, st2 = self.extended_gcd(a, p)
        if gcd != 1:
            raise ValueError('a is not invertible modulo p')

        print(st1 % p) 
    
    def extended_gcd(self, a, b):
        s, si1 = 0, 1
        t, ti1 = 1, 0
        r, ri1 = b, a

        while r != 0:
            quotient = ri1 // r
            ri1, r = r, ri1 - quotient * r
            si1, s = s, si1 - quotient * s
            ti1, t = t, ti1 - quotient * t

        return ri1, si1, ti1
    
    def binaryExponention(self, a, b, p):       
        result = 1
        a = a % p
        while b > 0:
            if b & 1:
                result = (result * a) % p
            b = b >> 1
            a = (a * a) % p
        return result

