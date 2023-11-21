# RSA Algorithm

## Overview
`generate_keys.py` generates RSA public and private keys and saves them to separate files. It includes functions for checking prime numbers, finding the greatest common divisor using the Euclidean algorithm, and calculating the modular inverse.
`RSA.py` script provides functionality for encrypting and decrypting text using a basic implementation of the RSA algorithm. The RSA algorithm is a widely used public-key cryptosystem that relies on the mathematical properties of large prime numbers.

## Essential functions

### `euclidean(a, b)`
Calculates the greatest common divisor of two numbers `a` and `b` using the Euclidean algorithm.

```Python
def euclidean(a, b): 
    while b != 0:
        a, b = b, a % b
    return a
```

### `modulo_inverse(a, m)`
Finds the modular inverse of `a` modulo `m`.
$$ x \equiv a^{-1} \pmod{m} $$

```Python
def modulo_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1
 
```

### `encrypt(encrypted_text_path, plaintext_path)`

This function reads the public key from the 'public.key' file, reads the plaintext from the specified file and converts each character to its ASCII code. The most crucial part is line which raises to the power of the public key (e) with modulo (n).<br>
$$ c \equiv m^e \pmod{n} $$
Then saves the encrypted values to a file. 

```Python
for char in formatted_plaintext:
          encrypted_text.append(pow(int(char), public_key[0], public_key[1]))
```

### `decrypt(encrypted_text_path, decrypted_text_path)`

This function reads the private key from the 'private.key' file, reads the encrypted text from the specified file, decrypts each value using the private key using , and then saves the decrypted text to a file.
$$ m \equiv c^d \pmod{n} $$
### `plot_encrypted_text(encrypted_text, key)`

- **Input**: 
    - `encrypted_text` - List of encrypted values.
    - `key` - List containing two integers representing the public key.

This function generates a histogram of the encrypted values. It also adds vertical dashed lines at positions corresponding to the public key values 'e' and 'n'. The resulting histogram is saved as 'public/histogram.png'.

## Usage

The script can be run as a standalone program. It encrypts the text from 'text.txt', saves the encrypted values to 'text.enc', then decrypts the values from 'text.enc' and saves the decrypted text to 'text.dec'.

```python
if __name__ == '__main__':
     encrypted_text_path = 'src/texts/text.enc'
     decrypted_text_path = 'src/texts/text.dec'
     plaintext_path = 'src/texts/text.txt'

     encrypt(encrypted_text_path, plaintext_path)
     decrypt(encrypted_text_path, decrypted_text_path)
```

## Dependencies
- `matplotlib`: This library is used for plotting the histogram.


### Authors

Gabriela Godek

### License

This project is available for use under the MIT License.