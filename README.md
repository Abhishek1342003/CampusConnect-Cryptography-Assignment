# CampusConnect Cryptographic Protocol Assignment

## Programming Language

Python 3.12

---

# Task 1

RSA Algorithm

Implemented:

- Key Generation
- Encryption
- Decryption

Constraints

- p and q are distinct primes
- 0 ≤ m < n
- d is modular inverse of e

Test Cases

1.

p=3

q=11

m=4

2.

p=7

q=17

m=10

---

# Task 2

Diffie-Hellman Key Exchange

Implemented

- Public Key Generation
- Shared Secret Generation
- Key Verification

Worked Example

p=29

α=2

a=5

b=12

Additional Example

p=23

α=5

a=6

b=15

---

# Task 3

Security Principle Mapping

## RSA

Provides

- Confidentiality
- Authentication (when combined with signatures)
- Non-repudiation through digital signatures

RSA encrypts data using the recipient's public key so only the holder of the private key can decrypt it.

---

## Diffie-Hellman

Provides

- Secure Key Exchange

Diffie-Hellman establishes a shared secret over an insecure network. It is not an encryption algorithm because it only creates a common secret key; encryption must be performed separately using algorithms such as AES.

---

# Task 4

## (a)

Firewall Placement

The firewall should be placed between the Internet and CampusConnect servers.

Recommendation

Hardware firewall.

Rule

Allow only HTTPS (TCP Port 443).

Block Telnet (TCP Port 23).

---

## (b)

IDS

Deploy both

Host-based IDS

Detects unauthorized file modifications and suspicious local processes.

Network-based IDS

Detects malicious traffic, port scanning, and attacks across the network.

---

## (c)

HTTP or HTTPS

CampusConnect should use HTTPS.

HTTPS prevents

Credential sniffing

Session hijacking

Man-in-the-middle attacks

by encrypting communication between client and server.

---

## (d)

Authentication Design

Use Multi-Factor Authentication

Factors

1. Password

2. OTP through Authenticator App

Least Privilege

Student

- View courses
- Register courses
- View grades

Instructor

- Upload grades
- Manage attendance

Administrator

- User management
- Database administration
- System configuration

---

## (e)

Threat Model

Example

A hacker captures login traffic over an unsecured Wi-Fi network using a packet sniffer to steal usernames and passwords.

Classification

Passive Attack

Justification

The attacker only observes network traffic without modifying data or disrupting communication.
