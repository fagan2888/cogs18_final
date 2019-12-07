
# Fancy Encoding. 3 Original methods to encode messages.
# Attempt to decode message after encoding.

def reverse_encode(message):
    '''
    Encoder that converts the message in reverse order.
    
    Parameters
    ----------
    message : string
        text message to be encoded
    
    Returns
    -------
    output : string
        reversed message
        
    Doctests
    -------
    >>> message = 'hello'
    >>> reverse_encode(message)
    'olleh'
    
    '''
    
    encoded = ''
    
    # Reverse message character by character
    for i in range(len(message)-1, -1, -1):
        encoded += message[i]
    
    return encoded


def shift_encode(message, key):
    '''
    Encoder that shifts every character by user-defined key.
    
    Parameters
    ----------
    message : string
        text message to be encoded
    key : int
        value each character is being shifted
    
    Returns
    -------
    output : string
        encoded message
        
    Doctests
    -------
    >>> text = "hello"
    >>> s = 4
    >>> shift_encode(text, s)
    'lipps'
    
    '''
    
    output = ''
    
    # Traverse each character in message
    for i in range(len(message)):
        char = message[i]
        
        # Encrypt uppercase characters
        if (char.isupper()):
            output += chr((ord(char) + key - 65) % 26 + 65)
            
        # Encrypt lowercase characters
        else:
            output += chr((ord(char) + key - 97) % 26 + 97)
    
    return output

def fancy_encode(message):
    '''
    Encoder that reverses a message and then shifts 
    every character by user-defined key.
    
    Parameters
    ----------
    message : string
        text message to be encoded
    
    Returns
    -------
    output : string
        encoded message
        
    Doctests
    -------
    >>> text = "hello"
    >>> shift_encode(text, s)
    'sppil'
    
    '''
    
    # Apply reverse_encode and shift_encode on the message
    reversed_message = reverse_encode(message)
    shifted_message = shift_encode(reversed_message, 4)
    
    return shifted_message


def decode_attempt(message, letters):
    '''
    Decoder that shifts every character by every 
    key back to figure out original message.
    
    Parameters
    ----------
    message : string
        text message to be decoded
    key : int
        series of letters to decode message
    
    Returns
    -------
    output : string
        original message
        
    Doctests
    -------
    >>> text = "hello"
    >>> s = 4
    >>> encoded = shift_encode(text, s)
    >>> LETTERS
    >>> decode_attempt(encoded, )
    
    '''
    decoded = []
    for key in range(len(letters)):
        translated = ''
        for symbol in message:
            if symbol in letters:
                num = letters.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(letters)
                translated = translated + letters[num]
            else:
                translated = translated + symbol
        decoded.append(translater)
        print('Hacking key #%s: %s' % (key, translated))
    return decoded