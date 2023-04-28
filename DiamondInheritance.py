class A:
    attr = 1


class B(A):
    pass


class C(A):
    attr = 2


class D(B, C):
    pass


"""
# Явное устранение конфликтов
"""


class A1:
    attr = 1


class B1(A1):
    pass


class C1(A1):
    attr = 2


class D1(B1, C1):
    attr = A1.attr  # нарушается нормальный путь поиска при наследовании


"""
# Атрибуты также могут быть функциями метода
"""


class A2:
    def meth(s):
        print('A2.meth')


class C2(A2):
    def meth(s):
        print('C2.meth')


class B2(A2):
    pass


class D2(B2, C2):
    pass
    # meth = A2.meth (вывод A2. meth)


if __name__ == '__main__':
    x = D()
    print(x.attr)  # выдаст 2
    print(
        D.__mro__)  # Ищет в Python 3.X (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
    # Явное устранение конфликтов
    x = D1()
    print(x.attr)  # вдаст 1 ( мы явно указываем какой атрибут хотим видеть в D2
    # Атрибуты - функции метода
    x = D2()
    print(x.meth())  # C2.meth
