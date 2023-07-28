# ECC Elliptic curve cryptography 
in this Repo we will aim to answer multiple questions in the elliptic curves Cryptography, including relevant number theory procedures and use of elliptic curves for encryption, key exchange and digital signature by using python. 

## Inverse Euclidean algorithm 
### Finding the inverse value of an integer modulo P where P is a prime number
usually if some one asks you this question they will give you the question like following.
q: create or construct a program implementing euclidean algorithm in which the inputs are a and p where p is prime and a!=kp and the output is a^(-1) mod p
### Definition 
integer b is the inverse of integer a mod p where a.b = 1 mod p 
### Procedure 
the function `inverseModulo` will get two numbers namely a and p and it will calculate the inverse of a mod p using the function `extended_gcd`

## Fast Exponention
the aim of this function is to calculate a^(p-1) mod p in an efficient manner, we know that for prime number `p` the result for this calculation is always '1' but anyways we can double check using the exponention python' s 'pow' function with an additional third parameter which is modulo will automatically calculate very efficiently but the notion here is that usually we will need to calculate `np` for addition of points on elliptic curves and this idea of doing this in a binary way comes in handy for calculation.
### procedure 
normally to calculate a^p we dp ot as stated in the definition of power `a*a*a*a*...*a` (p-times) the trick is we calculate `{1,a, a^2, a^4, a^8, ...}` and only multiply those represented as 1's in the binary form. using the function `binaryExponention` instead of b you can put p-1 to obtain the expected result of 1. 
