import matplotlib.pyplot as plt
import pandas as pd

def get_key(file_path):
     with open(file_path, 'r', encoding='utf-8') as file:
          text = file.read().splitlines()
          keys = []
          for line in text:
               if line: 
                    keys.append(int(line))   
     return keys

def read_file(file_path):
     with open(file_path, 'r', encoding='utf-8') as file:
          content = file.read()
     return content

def write_file(file_path, content):
     with open(file_path, 'w') as file:
          file.write(content)

def encrypt(encrypted_text_path, plaintext_path):
     public_key_path = 'src/keys/public.key'

     public_key = get_key(public_key_path)
     plaintext = read_file(plaintext_path)
     
     formatted_plaintext = []
     for char in plaintext:
          formatted_plaintext.append(f'{ord(char):03}')
     
     encrypted_text = []   
     for char in formatted_plaintext:
          encrypted_text.append(pow(int(char), public_key[0], public_key[1]))

     print('Encrypted text:', encrypted_text)
     plot_encrypted_text(encrypted_text, public_key)
     write_file(encrypted_text_path, ','.join(map(str, encrypted_text)))

def decrypt(encrypted_text_path, decrypted_text_path):
     private_key_path = 'src/keys/private.key'

     private_key = get_key(private_key_path)
     encrypted_text = read_file(encrypted_text_path).split(',')

     decrypted_blocks = []
     for char in encrypted_text:  
          decrypted_blocks.append(chr(pow(int(char), private_key[0], private_key[1])))
     decrypted_text = ''.join(decrypted_blocks)

     write_file(decrypted_text_path, decrypted_text)

def plot_encrypted_text(encrypted_text, key):
     plt.hist(encrypted_text, bins=50, color='skyblue', edgecolor='black')

     plt.axvline(x=key[0], color='red', linestyle='dashed', linewidth=2, label='e')
     plt.axvline(x=key[1], color='green', linestyle='dashed', linewidth=2, label='n')

     plt.title('Histogram of Encrypted Text')
     plt.xlabel('Encrypted Value')
     plt.ylabel('Frequency')
     plt.legend()
     plt.savefig('public/histogram.png')
     
     
if __name__ == '__main__':
     encrypted_text_path = 'src/texts/text.enc'
     decrypted_text_path = 'src/texts/text.dec'
     plaintext_path = 'src/texts/text.txt'

     encrypt(encrypted_text_path, plaintext_path)
     decrypt(encrypted_text_path, decrypted_text_path)
     
     
     