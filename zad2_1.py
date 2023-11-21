def encode(text, shift):
    mod = 256 # Full UNICODE range
    code_text = ''
    for char in text:
        code = ord(char)
        if char.isalpha() or char.isdigit():
            if char.islower():
                code_text += chr((code - ord('a') + shift) % mod + ord('a'))
            elif char.isupper():
                code_text += chr((code - ord('A') + shift) % mod + ord('A'))
            elif char.isdigit():
                code_text += chr((code - ord('0') + shift) % mod + ord('0'))
        else:
            code_text += char
    
    return code_text


def decode(text, shift):
    mod = 256 # Full UNICODE range
    code_text = ''
    for char in text:
        code = ord(char)
        if char.isalpha() or char.isdigit():
            if char.islower():
                code_text += chr((code - ord('a') - shift) % mod + ord('a'))
            elif char.isupper():
                code_text += chr((code - ord('A') - shift) % mod + ord('A'))
            elif char.isdigit():
                code_text += chr((code - ord('0') - shift) % mod + ord('0'))
        else:
            code_text += char
    
    return code_text


choice = input('What do you want to do? Choose (c) for coding message or (d) for decoding: ')
if choice.lower() == 'c' or choice.lower() == 'd':
    text = input('Text: ')
    key = int(input('Key: '))
    
    if choice == 'c':
        encode_text = encode(text, key)
        print(f'Encoded text: {encode_text}')
    elif choice == 'd':
        decode_text = decode(text, key)
        print(f'Decoded text: {decode_text}')
else: 
    print('Error: Choose the correct action (c or d)')
