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
### Procedure 
normally to calculate a^p we dp ot as stated in the definition of power `a*a*a*a*...*a` (p-times) the trick is we calculate `{1,a, a^2, a^4, a^8, ...}` and only multiply those represented as 1's in the binary form. using the function `binaryExponention` instead of b you can put p-1 to obtain the expected result of 1.

## Number of points on an Elliptic curve
We will consider `E: Y^2 = x^3 + ax +b mod p` as our elliptic curve and the aim is to count the number of points on this curve, calculation of every possible x is going to yield some t but we should check if this t has an square root modulo p. for every prime number `p` we know that `a^(p-1) =1 mod p`, in order to check if t has a square root mod p we only need to check the condition `t^((p-1)/2) =1 mod p` if this condition is satisfied then both (-sqrt(t),+sqrt(t)) and their respective x are points on the curve. 
### Procedure
since p is prime we compute equation for all the possible x mod p
then we check the answer of each equation to see if they have square root mod p 
if they have we add two points in our counter ( x,-y) (x,y)
and finally we add infinity as a point on the curve(dont worry addition of infinity to our set of points is very useful and meaningful). to run the code execute count_curve_points with a,b,p variables and you will get an answer. however for large p's this may not be an efficient way

## Determining all the possible curves
In order to determine all the possible curves mod p where p is prime number we need to check `4*a^3 + 27* b^2 ≠ 0 mod p` condition where we consider our elliptic curve to be in the form of `y^2 = x^3+ax+b` and we will determing their orders using the method we provided for counting the numbers on the curve

### Procedure
we loop through all the possible variables for a and b modulo p and we will check the condition one by one.  
