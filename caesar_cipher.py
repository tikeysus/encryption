'''
This function will cover the simple Caesar Cipher encryption technique. 
For the sake of simplicity, the given string will be converted to lowercase characters
and will only deal with English letters and not digits or any other symbols.  
'''

from exceptions import UnsupportedCharacterError

def caesar_cipher_encoder(message, key = 3): # -> By default, the key is three, Caesar would be proud. 
    if not message:
        return '' 

    message = list(message.lower())

    try:

        for i in range(len(message)):
            if message[i] == ' ':
                message[i] = ' '
            
            elif ord(str(message[i])) < 97 or ord(str(message[i])) > 122:
                raise UnsupportedCharacterError

            elif ord(str(message[i])) >= 122 - key:
                message[i] = chr(97 + key - (122 - ord(str(message[i]))) - 1)
            
            else:
                message[i] = chr(ord(str(message[i])) + key)

    except UnsupportedCharacterError:
        return "The text contains a character that is not supported by this algorithm."

    except Exception as e:
        return f'An exception {e} occured.'
    
    return ''.join(message)

print(caesar_cipher_encoder('bratan priveT 4', 5))
