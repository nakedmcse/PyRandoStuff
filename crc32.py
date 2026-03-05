# Implementation of crc32 in python
from typing import List

def make_crc32_table(poly: int) -> List[int]:
    crc32_table = [0 for _ in range(256)]
    i = 128
    crc32 = 1
    while i > 0:
        crc32 = (crc32 >> 1) ^ (poly if crc32 & 1 else 0)
        for j in range(0,255,2*i):
            crc32_table[i+j] = crc32 ^ crc32_table[j]
        i = i >> 1
    return crc32_table

def get_crc32(data: bytes, init: int, crc32_table: List[int]) -> int:
    crc32 = init
    for c in data:
        crc32 = crc32 ^ c
        crc32 = (crc32 >> 8) ^ crc32_table[crc32 & 0xFF]
    return crc32 ^ 0xFFFFFFFF

test_str = "1234567890"
test_bytes = bytes(test_str.encode("ascii"))
table = make_crc32_table(0x82F63B78)
print(hex(get_crc32(test_bytes, 0xFFFFFFFF, table)))