# WyborKluczy
import random
import json

def is_prime(n, i = 2):
    if (n == 0 or n == 1):
        return False
    if (n == i):
        return True
    if (n % i == 0):
        return False

    return is_prime(n, i + 1)
 
 
def euclidean(a, b): 
    if a == 0: 
        return b, 1, 0
             
    gcd, x1, y1 = euclidean(b % a, a) 
     
    x = y1 - (b // a) * x1 
    y = x1 
     
    return gcd, x, y 

def modulo_inverse(a, m):
    g, x, y = euclidean(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m
     
 
a, b = int(random.random() * 10), int(random.random() * 10)
g, x, y = euclidean(a, b) 
    

def generate_key_pair():
    p = int(random.random() * 10)
    q = int(random.random() * 10)

    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    
    while euclidean(e, phi)[0] != 1:
        e = random.randint(2, phi - 1)

    d = modulo_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

public_key, private_key = generate_key_pair()

print("Public key (e, n):", public_key)
print("Private key (d, n):", private_key)

with open('public.key', 'w') as file:
     file.write(json.dumps(public_key))
with open('private.key', 'w') as file:
     file.write(json.dumps(private_key))
     
     
print(is_prime(45))