class Adder:
    def __init__(self, data):
        self.data = data
    
    def add(self, y):
        raise NotImplemented
    
    def __add__(self, other):
        raise NotImplemented


class ListAdder(Adder):
    def add(self, y):
        return [self.data] + [y]
    
    def __add__(self, other):
        return [self.data] + [other]


class DictAdder(Adder):
    def add(self, y):
        return {self.data: 'First', y: 'Second'}
    
    def __add__(self, other):
        return {self.data: 'First', other: 'Second'}


if __name__ == '__main__':
    b = ListAdder(2)
    print(b.add(3))
    c = DictAdder(3)
    print(c+4)
    
