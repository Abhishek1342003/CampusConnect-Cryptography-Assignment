import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

def rsa(p, q, m):

    if p == q:
        print("Error: p and q must be different primes.")
        return

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    d = mod_inverse(e, phi)

    if m >= n:
        print("Message must satisfy 0 <= m < n")
        return

    c = pow(m, e, n)
    recovered = pow(c, d, n)

    print("\n------ RSA ------")
    print("p =", p)
    print("q =", q)
    print("n =", n)
    print("phi(n) =", phi)
    print("e =", e)
    print("d =", d)
    print("Encrypted =", c)
    print("Decrypted =", recovered)


print("Test Case 1")
rsa(3,11,4)

print("\nTest Case 2")
rsa(7,17,10)
