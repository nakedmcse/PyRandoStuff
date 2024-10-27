# Example of breaking repeating xor
from itertools import combinations


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
    key_length = 0

    for keysize in range(2, len(text) // 4):
        chunks = [text[start:start + keysize] for start in range(0, len(text), keysize)]
        subgroup = chunks[:4]
        # getting the average hamming distance per byte
        average_score = (sum(hamming_distance(a, b) for a, b in combinations(subgroup, 2)) / 6) / keysize
        if average_score < min_score:
            min_score = average_score
            key_length = keysize

    return key_length


input_text = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
xor_key = b"ICEBABY123"

encoded_text = xor_repeating_encode(input_text, xor_key)
recovered_keylen = find_key_length(encoded_text)
print(hamming_distance(b'this is a test',b'wokka wokka!!!'))
print(f'Recovered key length: {recovered_keylen}')