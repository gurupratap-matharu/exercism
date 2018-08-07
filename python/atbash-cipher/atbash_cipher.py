Plain = 'abcdefghijklmnopqrstuvwxyz'
Cipher = 'zyxwvutsrqponmlkjihgfedcba'

encode_map = dict(zip(Plain, Cipher))
decode_map = dict(zip(Cipher, Plain))


def encode(plain_text):
    """
    Encodes the plain text into cipher text based on the atbash cipher algorithm.
    Returns the cipher as a string.
    """
    text = plain_text.lower()  # First we convert to lowercase
    text = ''.join([x for x in text if x.isdecimal() or x.isalpha()])  # We remove the punctuation marks and only accept decimals and alphabets.

    lst = [encode_map[x] if encode_map.get(x) else x for x in text]  # Take relevant ciphers from our mapping dictionary.
    for count in range(5, len(lst) + 1, 6):  # Loop to add spaces after every 5 chunks.
        lst.insert(count, ' ')
    return ''.join(lst)


def decode(ciphered_text):
    """
    Decodes the ciphered text into human readable text.
    Returns a string.
    """
    text = ciphered_text.replace(' ', '')  # We remove all whitespaces
    return ''.join([decode_map[x] if decode_map.get(x) else x for x in text])
