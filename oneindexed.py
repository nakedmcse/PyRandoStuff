class OneIndexedList(list):
    def __getitem__(self, index):
        if index == 0:
            raise IndexError("Index 0 is invalid.")
        return super().__getitem__(index - 1)

    def __setitem__(self, index, value):
        if index == 0:
            raise IndexError("Index 0 is invalid.")
        super().__setitem__(index - 1, value)

    def __delitem__(self, index):
        if index == 0:
            raise IndexError("Index 0 is invalid.")
        super().__delitem__(index - 1)

    def insert(self, index, value):
        if index == 0:
            raise IndexError("Index 0 is invalid.")
        super().insert(index - 1, value)

# Create one indexed list
arr = OneIndexedList(['a', 'b', 'c'])
try:
    print(arr[1])       # 'a'
    print(arr[2])       # 'b'
    print(arr[3])       # 'c'
    print(arr[0])       # Raises index exception - no 0
except Exception as e:
    print(e)

arr.append('d')
print(arr[4])           #'d'
print(len(arr))         # len returns 4