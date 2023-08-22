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
    
    def binaryExponention(self, a:int,b:int, p:int):       
        result = 1
        a = a % p
        while b > 0:
            if b & 1:
                result = (result * a) % p
            b = b >> 1
            a = (a * a) % p
        return result
    
    def comp_vurve_modp(self, x, a, b, p):
        t = pow(x, 3) + a*x + b
        s = t % p
        if (pow(s, int((p-1)/2), p) == 1):
            return True
        else:
            return False
        
    def count_curve_points(self, a, b, p):
        nop = 1
        for x in range(p):
            if (self.comp_vurve_modp(x, a, b, p)):
                nop = nop+2
        print("number of points on the curve is: {}".format(nop))
        return nop
    

    def deter_possible_curves(self, p=23):
        for a in range(p):
            for b in range(p):
                # checking the validity of the combination
                if ((4*pow(a, 3) + 27*pow(b, 2)) % p != 0):
                    """calculate the order"""
                    """print the curve formula and its order"""
                    print("curve E: y^2 = x^3 + {}x + {} mod {}".format(a, b, p))
                    self.count_curve_points(a, b, p)
                    print("\n")
                else:
                    print(
                        "{} and {} are not suitable to make an elliptic curve".format(a, b))
    
    def image_message(self,m , a, b, p):
        x = m % p
        y_squared = (pow(x,3)+ a*x + b) % p
        y = pow(y_squared, (p+1)/2, p) 
        return (x,y)
