import json

# with open('./src/original-text.txt', 'r', encoding='utf-8') as file:
#     crypto = file.read()


mod = 46
def code(text, shift):
    codeText = ''
    for letter in text:
        if ord(letter) == 32:
            codeText += letter
        elif letter.islower():
            codeText += chr((ord(letter) + shift - 97) % mod + 97)
        elif letter.isupper():
            codeText += chr((ord(letter) + shift - 65) % mod + 65)
        else:
            codeText += chr((ord(letter) + shift - 65) % mod + 65)
            
    
    return codeText


def decode(text, shift):
    codeText = ''
    for letter in text:
        if ord(letter) == 32:
            codeText += letter
        elif letter.islower():
            codeText += chr((ord(letter) - shift - 97) % mod + 97)
        else:
            codeText += chr((ord(letter) - shift - 65) % mod + 65)
    
    return codeText


choice = input('What to do? Choose c or d: ')
if choice == 'c' or choice == 'd':
    text = input('Text: ')
    key = int(input('Key: '))
    
    if choice == 'c':
        decodeText = code(text, key)
    elif choice == 'd':
        decodeText = decode(text, key)
    print(decodeText)
else: 
    print('Error')

