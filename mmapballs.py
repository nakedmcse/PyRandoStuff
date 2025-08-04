import mmap
import os

file_path = "example.txt"
with open(file_path, "wb") as f:
    f.write(b"This is some sample text for mmap demonstration.")

with open(file_path, "r+b") as f_obj:
    with mmap.mmap(f_obj.fileno(), 0) as mm:
        print(f"Initial position: {mm.tell()}")

        mm.seek(10)
        print(f"Position after seeking to 10: {mm.tell()}")

        mm.read(5)
        print(f"Position after reading 5 bytes: {mm.tell()}")

os.remove(file_path)