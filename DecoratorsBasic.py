"""
Декораторы - разновидность объявления во время выполнения следующих за ними функций
Записывается перед опервтором def
Состоит из символа @ ( называется метафункцией)


"""


class C:
    @staticmethod
    def meth():
        pass


"""
Альтернативная реализация синтаксиса

"""


class K:
    def meth():
        pass
    
    meth = staticmethod(meth)


"""
Благодаря декорированию получается лучший способ реализации
со статистическим методом

"""


class Spam:
    numInstances = 0
    
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1
    
    @staticmethod
    def printNumInstances():
        print('Number of instances created: %s' % Spam.numInstances)  # количество созданных экземпляров


"""
Реализация classmethod, ststicmethod, property

"""


class Methods:
    def imeth(self, x):
        print(self, x)
    
    @staticmethod  # по прежнему называются методами
    def smeth(x):
        print([x])
    
    @classmethod
    def cmeth(cls, x):
        print([cls, x])
    
    @property
    def name(self):
        return 'Bob ' + self.__class__.__name__


"""
Декораторы функций, определяемые пользователем

"""


class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    
    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args)


@tracer
def spam(a, b, c):
    return a + b + c


# Другая реализация декораторов

def tracer(func):
    def wrapper(*args):
        wrapper.calls += 1
        print('call %s to %s' % (wrapper.calls, func.__name__))
        return func(*args)
    
    wrapper.calls = 0
    return wrapper


class H:
    @tracer
    def spam(self, a, b, c):
        return a + b + c


"""
Реализация декораторв класса

"""


def decorator(cls):
    class Proxy:
        def __init__(self, *args):
            self.wraped = cls(*args)
        
        def __getattr__(self, item):
            return getattr(self.wraped, name)
    
    return Proxy


@decorator
class F:
    pass


if __name__ == '__main__':
    a = Spam()
    b = Spam()
    c = Spam()
    Spam.printNumInstances()
    a.printNumInstances()
    
    # Реализация методов в декораторах
    
    obj = Methods()
    print(obj.imeth(1))
    print(obj.imeth(2))
    print(obj.imeth(3))
    print(obj.name)
    
    # Декоратор функций, определяемый пользователем
    print(spam(1, 2, 3))
    print(spam('a', 'b', 'c'))
    k = H()
    print(k.spam(1, 2, 3))
    print(k.spam('a', 'b', 'c'))
    
    # Декоратор классов
    a = F()
    print(a)
