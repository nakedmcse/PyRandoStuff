class Dummy:

    my_list = []

    def surprise(self, x):
        print(self.my_list)
        self.my_list.append(x)


one = Dummy()
two = Dummy()

one.surprise('x')       # ok python
two.surprise('x')       # wtf python...