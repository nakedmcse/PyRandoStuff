from typing import List
import zlib, time

inverse_key_table = [
    0x37, 0x6a, 0x09, 0x5e, 0x7a, 0xaf, 0xf5, 0xa4, 0xba, 0x78, 0x84, 0x58, 0x35, 0x1e, 0x6b, 0x0c,
    0x49, 0xc6, 0xc3, 0x44, 0x40, 0x9e, 0x6f, 0x65, 0xe4, 0xf6, 0xfe, 0x22, 0xe2, 0x95, 0xc7, 0x38,
    0xf0, 0x1a, 0x82, 0xe0, 0x5b, 0x2a, 0xd8, 0xe5, 0xce, 0x2f, 0x74, 0x25, 0xec, 0x59, 0xc0, 0x45,
    0x4b, 0x64, 0x43, 0xdc, 0xb0, 0xb9, 0x30, 0x6d, 0x28, 0xd1, 0x16, 0xbb, 0x66, 0x98, 0x92, 0x90,
    0x2c, 0xa7, 0xf1, 0x80, 0xc1, 0xd4, 0x8b, 0xd6, 0xdf, 0x24, 0x2d, 0xf7, 0xfb, 0x88, 0x4d, 0x3c,
    0x72, 0xf3, 0xdb, 0x2b, 0x93, 0x73, 0xef, 0x85, 0x83, 0xee, 0xc2, 0x8d, 0x5c, 0xb2, 0x0b, 0x94,
    0x3d, 0xa8, 0x3f, 0x1c, 0x4c, 0x6e, 0x03, 0x7b, 0x1d, 0x5a, 0x51, 0xa1, 0x70, 0x41, 0xd0, 0xaa,
    0xa0, 0x7e, 0xcd, 0xd5, 0x15, 0xa9, 0x18, 0x76, 0xc9, 0x7d, 0x7f, 0x0e, 0x3a, 0x99, 0xbf, 0xab,
    0x3b, 0x14, 0x3e, 0x9a, 0x04, 0xda, 0x02, 0xfd, 0x63, 0xd9, 0xfa, 0x9f, 0x4e, 0xe3, 0x61, 0xbe,
    0x07, 0x11, 0xa6, 0x1b, 0x19, 0x55, 0x8e, 0x77, 0x0a, 0x47, 0xe6, 0xf8, 0x0d, 0xcf, 0xd7, 0x33,
    0x23, 0x1f, 0xbc, 0x62, 0xde, 0x9b, 0x29, 0x53, 0x68, 0xe8, 0x21, 0xb6, 0x34, 0x52, 0x87, 0xcb,
    0x08, 0x79, 0xf4, 0x67, 0x69, 0x54, 0xe7, 0x86, 0xea, 0xb4, 0x20, 0x71, 0x01, 0xbd, 0x06, 0x31,
    0x00, 0x50, 0xc8, 0xb8, 0xac, 0x5d, 0x57, 0x7c, 0x89, 0xeb, 0xb7, 0x36, 0x8f, 0xf2, 0xe1, 0x56,
    0x81, 0x4a, 0xd2, 0x8c, 0xf9, 0xad, 0x60, 0xa5, 0x42, 0x10, 0x5f, 0x12, 0xb3, 0xff, 0x4f, 0xdd,
    0x46, 0x26, 0xa2, 0x17, 0xc5, 0x75, 0x91, 0x27, 0xb5, 0x8a, 0xd3, 0x13, 0x2e, 0xc4, 0xe9, 0x9d,
    0x97, 0x39, 0x32, 0x05, 0x0f, 0xca, 0xcc, 0x48, 0xfc, 0xae, 0x96, 0xed, 0x6c, 0x9c, 0xb1, 0xa3,
]

pass_1_xor_bytes = [0x45, 0x71]
pass_2_xor_bytes = [0x86, 0x23]

pass_1_predefined = [
    165, 176, 167, 250, 214, 93, 241, 128, 249, 138, 77, 60, 85, 174, 134, 92,
    2, 226, 244, 158, 130, 3, 90, 170, 195, 45, 229, 122, 159, 242, 252, 179,
    31, 61, 10, 114, 217, 76, 109, 78, 48, 1, 219, 161, 43, 108, 208, 32,
    216, 100, 7, 105, 15, 209, 164, 188, 232, 75, 218, 206, 12, 184, 127, 14,
    222, 11, 213, 132, 27, 70, 47, 120, 111, 68, 125, 26, 9, 203, 41, 245,
    239, 49, 20, 30, 183, 56, 53, 178, 228, 147, 73, 182, 135, 149, 83, 143,
    91, 42, 148, 169, 107, 129, 145, 243, 40, 157, 52, 177, 94, 191, 84, 5,
    200, 193, 28, 65, 21, 58, 173, 50, 233, 23, 225, 227, 160, 89, 202, 103,
    44, 221, 13, 38, 33, 113, 201, 185, 131, 254, 39, 144, 154, 248, 71, 198,
    220, 136, 212, 17, 59, 240, 253, 163, 142, 194, 172, 62, 97, 51, 99, 46,
    4, 180, 86, 224, 87, 55, 102, 211, 181, 95, 236, 152, 251, 196, 98, 162,
    187, 126, 57, 189, 72, 230, 116, 67, 237, 29, 210, 192, 223, 141, 156, 231,
    171, 117, 140, 115, 101, 74, 235, 79, 146, 63, 207, 16, 168, 18, 238, 139,
    36, 104, 6, 255, 96, 118, 106, 215, 190, 124, 66, 166, 54, 123, 137, 151,
    234, 175, 34, 88, 110, 82, 19, 205, 35, 69, 186, 246, 153, 25, 199, 80,
    37, 24, 247, 150, 8, 121, 22, 133, 204, 112, 64, 119, 197, 155, 0, 81
]

pass_2_predefined = [
    33, 222, 39, 249, 29, 185, 24, 55, 66, 157, 109, 192, 217, 188, 64, 250,
    173, 84, 58, 118, 133, 56, 36, 50, 244, 16, 46, 236, 197, 219, 41, 100,
    10, 112, 253, 184, 159, 65, 0, 60, 164, 232, 23, 113, 2, 149, 75, 203,
    196, 165, 74, 119, 215, 68, 43, 90, 37, 18, 34, 158, 3, 82, 201, 151,
    116, 95, 143, 126, 235, 155, 35, 115, 194, 117, 172, 209, 148, 21, 170, 200,
    67, 134, 218, 142, 241, 175, 162, 105, 108, 254, 144, 220, 124, 49, 97, 51,
    178, 4, 230, 86, 129, 52, 101, 5, 202, 190, 13, 231, 240, 48, 150, 169,
    239, 107, 44, 233, 17, 38, 180, 26, 146, 128, 79, 191, 181, 206, 223, 141,
    214, 135, 89, 140, 42, 125, 20, 73, 72, 47, 22, 61, 167, 123, 153, 91,
    76, 70, 99, 189, 224, 103, 106, 229, 228, 27, 193, 182, 221, 1, 199, 213,
    251, 198, 120, 9, 161, 195, 211, 57, 227, 102, 207, 122, 87, 6, 237, 12,
    19, 78, 147, 154, 96, 255, 104, 71, 177, 179, 69, 187, 53, 152, 11, 242,
    168, 245, 226, 247, 210, 163, 15, 132, 110, 31, 216, 171, 14, 212, 252, 7,
    204, 166, 176, 80, 248, 8, 81, 208, 40, 183, 127, 145, 225, 174, 160, 205,
    32, 88, 111, 77, 28, 63, 30, 139, 243, 137, 83, 98, 114, 130, 62, 121,
    59, 85, 54, 138, 238, 246, 131, 93, 156, 136, 25, 186, 92, 45, 234, 94
]


def build_translation_table(xor_bytes: List[int], key_table: List[int]) -> List[int]:
    translation_table: List[int] = []
    for i in range(256):
        translation_table.append(key_table[i ^ xor_bytes[0]] ^ xor_bytes[1])
    return translation_table

def decode_on2_file(file_path: str) -> bytes:
    #pass_1_table = build_translation_table(pass_1_xor_bytes, inverse_key_table)
    #pass_2_table = build_translation_table(pass_2_xor_bytes, inverse_key_table)
    with open(file_path, "rb") as file:
        file_content = file.read()
        if file_content[0:4].decode("ascii") != 'ONS2':
            raise RuntimeError(f"File {file_path} does not contain ONS2 data")
        compressed_length = int.from_bytes(file_content[4:8], byteorder='little')
        original_length = int.from_bytes(file_content[8:12], byteorder='little')
        version = int.from_bytes(file_content[12:16], byteorder='little')
        print(f'Compressed length: {compressed_length}, original length: {original_length}, version: {version}')

        compressed_data = [0] * compressed_length
        for i in range(compressed_length):
            compressed_data[i] = pass_2_predefined[file_content[16 + i]]

        expanded_data = zlib.decompress(bytearray(compressed_data))
        final_data = [0] * original_length
        for i in range(original_length):
            final_data[i] = pass_1_predefined[expanded_data[i]]

        return bytearray(final_data)

start = time.time()
decoded_data = decode_on2_file("on2test-en.file")
end = time.time()
print(decoded_data.decode('utf-8')[0:200])
print()
print(f'Decoded length: {len(decoded_data)} in {(end - start)*1000:.4f} ms')