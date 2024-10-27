# Example of breaking repeating xor
import base64
from itertools import combinations, zip_longest


def assign_score(output_string):
    string_score = 0
    freq = [' ', 'e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u']
    for letter in output_string:
        if letter in freq:
            string_score += 1
    return string_score


def xor_decode_bytes(encoded_array):
    last_score = 0
    greatest_score = 0
    for n in range(256): # checks for every possible value for XOR key
        xord_str = [byte ^ n for byte in encoded_array]
        xord_ascii = ('').join([chr(b) for b in xord_str])
        last_score = assign_score(xord_ascii)
        if (last_score > greatest_score):
            greatest_score = last_score
            key = n
    return key


def xor_repeating_encode(input_string: bytes, key: bytes) -> bytes:
    output = []
    print(input_string)
    for i in range(len(input_string)):
        output.append(input_string[i] ^ key[i % len(key)])

    return bytes(output)


def hamming_distance(string1: bytes, string2: bytes) -> int:
    distance = 0
    for (byte1, byte2) in zip(string1, string2):
        distance += bin(byte1 ^ byte2).count('1')
    return distance


def find_key_length(text: bytes) -> int:
    # we are searching for the length that produces an output with the lowest hamming score
    min_score = len(text)
    max_key_len = len(text) // 4 if len(text) // 4 < 40 else 40
    key_length = 0

    for keysize in range(2, max_key_len):
        chunks = [text[start:start + keysize] for start in range(0, len(text), keysize)]
        subgroup = chunks[:4]
        # getting the average hamming distance per byte
        average_score = (sum(hamming_distance(a, b) for a, b in combinations(subgroup, 2)) / 6) / keysize
        if average_score < min_score:
            min_score = average_score
            key_length = keysize

    return key_length


def find_key(text: bytes, key_length: int) -> str:
    key_blocks = [text[start:start + key_length] for start in range(0, len(text), key_length)]
    # transpose the 2D matrix
    key = []
    single_xor_blocks = [list(filter(None,i)) for i in zip_longest(*key_blocks)]
    for block in single_xor_blocks:
        key_n = xor_decode_bytes(block)
        key.append(key_n)

    ascii_key = ''.join([chr(c) for c in key])
    return ascii_key

input_text = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
xor_key = b"ICEBABY123"

encoded_text = xor_repeating_encode(input_text, xor_key)

print(hamming_distance(b'this is a test',b'wokka wokka!!!'))

with open('/Users/walker/Documents/Code/TSCryptopals/set1q6.txt', 'r') as file:
    text = base64.b64decode(file.read())

recovered_keylen = find_key_length(text)
recovered_key = find_key(text, recovered_keylen)
print(f'Recovered key length: {recovered_keylen}')
print(f'Recovered key: {recovered_key}')
