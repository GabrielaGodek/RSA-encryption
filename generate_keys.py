import random
import math
import os

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modulo_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_number():
    return random.randrange(1, 10**9 + 1)

def generate_keys():
    p = generate_number()
    q = generate_number()
    while not is_prime(p):
        p = generate_number()

    while not is_prime(q) or q == p:
        q = generate_number()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1) if phi > 2 else 2
    while euclidean(e, phi) != 1:
        e = random.randint(2, phi - 1) if phi > 2 else 2

    d = modulo_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

def save_keys(key, filename):
    folder = 'src/keys'
    os.makedirs(folder, exist_ok=True)
    with open(f"{folder}/{filename}", 'w') as file:
        for n in key:
            file.write(f"{n}\n")

public_key, private_key = generate_keys()

print("Public key (e, n):", public_key)
print("Private key (d, n):", private_key)

save_keys(public_key, 'public.key')
save_keys(private_key, 'private.key')
