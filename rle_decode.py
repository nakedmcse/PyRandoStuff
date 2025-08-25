import re

def rle_decode(text: str) -> str:
    pattern = re.compile(r'(\d+)\[([^\[\]]+)\]')
    while re.search(pattern, text): text = re.sub(pattern, lambda m: int(m.group(1)) * m.group(2), text)
    return text

print(rle_decode('3[a]2[bc]'))