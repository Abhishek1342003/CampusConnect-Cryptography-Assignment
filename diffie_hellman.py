def diffie(p, alpha, a, b):

    A = pow(alpha, a, p)

    B = pow(alpha, b, p)

    KA = pow(B, a, p)

    KB = pow(A, b, p)

    print("\n----- Diffie Hellman -----")

    print("Public Prime =", p)

    print("Primitive Root =", alpha)

    print("Alice Public Key =", A)

    print("Bob Public Key =", B)

    print("Alice Shared Key =", KA)

    print("Bob Shared Key =", KB)

    if KA == KB:
        print("Keys Match")
    else:
        print("Keys Do Not Match")


print("Worked Example")
diffie(29,2,5,12)

print("\nTest Case 2")
diffie(23,5,6,15)
