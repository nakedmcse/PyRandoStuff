# Stupid Python Tricks
class Tricky:
    def __init__(self,value):
        self._value = value

    def __eq__(self,other):
        self._value += 1
        return self._value == other
    
a = Tricky(0)

if a == 1 and a == 2 and a == 3: print("Yes, it does")