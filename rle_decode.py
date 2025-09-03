def rle_decode(text: str, c_num: int = 0, c_str: str = '') -> str:
    stack = []

    for char in text:
        if char.isdigit(): c_num = c_num * 10 + int(char)
        elif char == '[':
            stack.append((c_str, c_num))
            c_str = ''
            c_num = 0
        elif char == ']':
            last_str, num = stack.pop()
            c_str = last_str + num * c_str
        else: c_str += char

    return c_str

print(rle_decode('3[a]2[bc]'))
print(rle_decode('3[a2[c]]'))