class C:
    """
    Перехват атрибутов ( пример )
    """
    data = 'spam'
    
    def __getattr__(self, item):  # В Python 3.X не работает
        print(item)
        
        return getattr(self.data, item)


class B(object):
    pass


"Перехват атрибутов"


class D(object):
    def __getattr__(self, item):
        print(item)


"Требование к написанию кода-посредника ( реалистичный сценарий)"


class Realistic(object):
    data = 'spam'
    
    def __getattr__(self, item):
        print('getattr: ' + item)
        return getattr(self.data, item)


class C1(object):
    data = 'spam'
    
    def __getattr__(self, item):
        print('getattr:' + item)
        return getattr(self.data, item)
    
    def __getitem__(self, item):
        print('getitem ' + str(item))
        return self.data[item]
    
    def __add__(self, other):
        print('add: ' + other)
        return getattr(self.data, '__add__')(other)


if __name__ == '__main__':
    X = C1()
    print(X.upper)
    print(X.upper())
    print(X[1])
    print(X.__add__('eggs'))
